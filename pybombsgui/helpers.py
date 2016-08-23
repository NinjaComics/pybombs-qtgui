#!/usr/bin/env python

import subproccess

def notify_send(summary, notif_msg, status=False):
    """Sends a notification to the system desktop-notification tray, if the
    package libnotify is installed
    """
    if status == True:
        subprocess.Popen(['notify-send', summary, notif_msg, '--icon=dialog-information'])
    else:
        subprocess.Popen(['notify-send', summary, notif_msg, '--icon=dialog-error'])


