#!/bin/python

from i3ipc import Connection

sway = Connection()

notifyd_windows = sway.get_tree().find_named("xfce4-notifyd")

modifier = 20

for notifyd_window in notifyd_windows:

    width = notifyd_window.geometry.width
    workspace_width = notifyd_window.workspace().rect.width
    
    x = workspace_width - width - 50
    y = modifier
    
    notifyd_window.command("move position {} {}".format(x, y))
    
    modifier += notifyd_window.geometry.height + 20
