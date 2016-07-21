#Pybombs imports
from pybombs import install_manager, package_manager, recipe, dep_manager,\
     pb_logging, recipe_manager, config_manager
from pybombs.pb_exception import PBException
from pybombs.recipe import Recipe

#PyQt imports
from PyQt5 import QtCore

#A class to generate the data for the main window
class DataGenerator(QtCore.QThread):
    data_generator = QtCore.pyqtSignal(list, list, list)

    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        """This is where we generate our data and provide a signal it to the GUI
        """
        #Init lists required to hold our data
        app_package_list = []
        sdk_package_list = []
        app_package_data = []
        sdk_package_data = []
        base_package_data = []

        pm = package_manager.PackageManager()
        #cfg = config_manager.config_manager
        #TODO Correctly list out recipes based on the prefix selected

        list_recipes = sorted(list(recipe_manager.recipe_manager.list_all()))

        for pkg_name in list_recipes:
            module = Recipe(recipe_manager.recipe_manager.
                            get_recipe_filename(pkg_name))
            if module.target == 'prefix':
                sdk_package_list.append(pkg_name)
            elif module.target == 'sdk':
                sdk_package_list.append(pkg_name)
            elif module.target == 'package':
                app_package_list.append(pkg_name)

        for pkg in sdk_package_list:
            rec = Recipe(recipe_manager.recipe_manager.get_recipe_filename(pkg))
            if rec.target == 'prefix':
                sdk_package_data.append([pkg, 'Prefix Specific Packages'])
            elif rec.target == 'sdk':
                sdk_package_data.append([pkg, 'SDK Packages'])

        for oot_module in app_package_list:
            rec = recipe.get_recipe(oot_module, target='package', fail_easy=True)
            if rec.category == 'baseline':
                if pm.installed(oot_module):
                    base_package_data.append([oot_module, 'Installed'])
                else:
                    base_package_data.append([oot_module, 'Not Installed'])
            else:
                if 'description' in rec.get_dict():
                    if pm.installed(oot_module):
                        app_package_data.append([oot_module,
                                                 rec.get_dict()['category'],
                                                 'Installed',
                                                 rec.get_dict()['description']])
                    else:
                        app_package_data.append([oot_module,
                                                 rec.get_dict()['category'],
                                                 'Not Installed',
                                                 rec.get_dict()['description']])
                else:
                    if pm.installed(oot_module):
                        app_package_data.append([oot_module,
                                                 rec.get_dict()['category'],
                                                 'Installed',
                                                 'No description available'])
                    else:
                        app_package_data.append([oot_module,
                                                 rec.get_dict()['category'],
                                                 'Not Installed',
                                                 'No description available'])

        self.data_generator.emit(app_package_data, base_package_data,
                                 sdk_package_data)
        return

#A worker thread that takes care of install/update/remove tasks
class AWorkerThread(QtCore.QThread):
    progress_tick = QtCore.pyqtSignal(int, int, str)
    error_info = QtCore.pyqtSignal(str)

    def __init__(self, package_list):
        QtCore.QThread.__init__(self)
        self.package_list = package_list

    def run(self):
        instaman = install_manager.InstallManager()

        if 'install' in self.package_list:
            install_list = self.package_list.get('install')
            try:
                for package in install_list:
                    instaman.install([package], 'install')
                    progress = (install_list.index(package)+1)/len(
                        install_list)*100.0
                    self.progress_tick.emit(progress, len(install_list), 'install')
            except Exception as ex:
                self.error_info.emit(str(ex))

        if 'update' in self.package_list:
            update_list = self.package_list.get('update')
            try:
                for package in update_list:
                    instaman.install([package], 'update', update_if_exists=True)
                    progress = (update_list.index(package)+1)/len(
                        update_list)*100.0
                    self.progress_tick.emit(progress, len(update_list), 'update')
            except Exception as ex:
                self.error_info.emit(str(ex))

        if 'remove' in self.package_list:
            try:
                remove_list = self.package_list.get('remove')
                pm = package_manager.PackageManager()
                dep_tree = dep_manager.DepManager().make_dep_tree(
                    self.package_list.get('remove'),
                    lambda x: bool(x in self.package_list.get('remove')))
                remove = reversed(dep_tree.serialize())
                ### Remove packages
                for pkg in remove:
                    #Uninstall:
                    pm.uninstall(pkg)
                    progress = (remove_list.index(pkg)+1)/len(remove_list)*100.0
                    self.progress_tick.emit(progress, len(remove_list), 'remove')
                    #Remove entry from inventory:
                    self.inventory.remove(pkg)
                    self.inventory.save()
            except Exception as ex:
                self.error_info.emit(str(ex))
        return

#Generic Thread for future use
class GenericThread(QtCore.QThread):
    def __init__(self, function, *args, **kwargs):
        QtCore.QThread.__init__(self)
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def __del__(self):
        self.wait()

    def run(self):
        self.function(*self.args, **self.kwargs)
        return
