#!/usr/bin/env python3

"""
This script aims to alert when the battery 
reaches a critical level in the system.
"""
import os


CRITICAL_BATTERY_PERCENTAGE = 8
CMD_NOTIFY_USER = "notify-send 'LOW BATTERY LEVEL' -u critical"


def check_battery_status():
    """Check main battery status."""
    battery_status = current_battery_status()
    battery_level = current_battery_level()

    if battery_status == "Discharging" and battery_level == CRITICAL_BATTERY_PERCENTAGE:
        notify_user()


def current_battery_level():
    """
    Return surrent system 
    battery level from:
    /sys/class/power_supply/BAT0/capacity
    """
    with open("/sys/class/power_supply/BAT0/capacity", "r") as battery_level:
        return int(battery_level.read())


def current_battery_status():
    """
    Return surrent system 
    battery status from:
    /sys/class/power_supply/BAT0/status
    """
    with open("/sys/class/power_supply/BAT0/status", "r") as battery_status:
        return battery_status.readline().strip()


def notify_user():
    """
    Notifies the user.
    $ notify-send "LOW BATTERY" -u critical
    """
    os.system("/bin/bash -c \"" + CMD_NOTIFY_USER + "\"")


if __name__ == "__main__":
    check_battery_status()
