#!/usr/bin/env python
#
# Copyright 2015 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# PyBOMBS is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# PyBOMBS is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyBOMBS; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#
"""
PyBOMBS - QtGUI
~~~~~~~~~~~~~~~

PyBOMBS (the Python Bundles Overlay Managed Build System) is a meta-package
manager that can install packages from source or using the local package
manager(s).

It was mainly designed for use by users of the `GNU Radio project`_, which
is extended by a large number of out-of-tree modules (OOTs).

PyBOMBS is a recipe-based system and can easily mix and match installations
from different sources. Cross-compilation works transparently.

PyBOMBS QtGUI is Qt based GUI frontend for the PyBOMBS package. It is developed
as a part of the Google Summer of Code 2016.

Basic Usage
-----------

With PyBOMBS installed, you might want to install GNU Radio and other OOT Modules
into a directory called 'my_prefix'. PyBOMBS-QtGUI extends the PYBOMBS command
line interface and provides a neat GUI to easily install GNU Radio and related
projects.

PyBOMBS/PYBOMBS-QtGUI will determine the dependency tree for GNU Radio, and
install dependencies either through the local system's package manager (e.g.
apt-get, yum, pip...) or pull the source files and build them in the
prefix.

For more informations see the `documentation`_.

.. _GNU Radio project: http://gnuradio.org/
.. _documentation: http://gnuradio.org/pybombs/
"""

from __future__ import print_function
try:
    import setuptools
except ImportError:
    print("=========================================================")
    print(" PyBOMBS requires setuptools for installing.             ")
    print(" You can install setuptools using pip:                   ")
    print("    $ pip install setuptools                             ")
    print("=========================================================")
    exit(1)

from setuptools import setup
#import qtgui

packages = [
    "pybombsgui",
    "pybombsgui.pyqtconvert",
]

package_data = {'resourses': ['pybombsgui/myicons_rc.py'],}

deps = [
    "pybombs",
]

setup(
    name="PyBOMBS-QtGUI",
    version='0.1.dev1',
    description="A meta-package manager to install software from source, or whatever "
                  "the local package manager is. Designed for easy install of source "
                  "trees for the GNU Radio project.",
    long_description=__doc__,
    url="http://gitlab.com/NinjaComics/",
    download_url="https://gitlab.com/NinjaComics/pybombs-qtgui",
    author="Ravi Sharan",
    author_email="bhagavathula.ravisharan@gmail.com",
    maintainer="Ravi Sharan",
    maintainer_email="bhagavathula.ravisharan@gmail.com",
    license="GPLv3",
    packages=packages,
    package_data=package_data,
    entry_points={
        'gui_scripts' : ['pybombsgui = pybombsgui.main_window:main',],
    },
    install_requires=deps,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.5",
        "Topic :: Communications :: Ham Radio",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Embedded Systems",
        "Topic :: System :: Archiving :: Packaging",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Software Distribution",
        "Topic :: Utilities",
    ],
    #zip_safe=False,
)
