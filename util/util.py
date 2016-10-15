""" Utility library for notes-cli """
import platform


def is_windows_machine():
    """ Detect if machine is running Windows"""
    return True if (platform.system() == 'Windows') else False
