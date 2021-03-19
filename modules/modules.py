import os
import getpass

def validator_path(path):
    if path is not None and os.path.exists(path):
        return 1
    else:
        return 0

def get_file_size(path):
    if validator_path(path):
        size = os.path.getsize(path)
        return size

def make_path():
    if os.name == "nt":
        try:
            os.mkdir("C:/Users/{}/Desktop/D3ViLDownloader/".format(getpass.getuser()))
            path = "C:/Users/{}/Desktop/D3ViLDownloader/".format(getpass.getuser())
        except FileExistsError:
            path = "C:/Users/{}/Desktop/D3ViLDownloader/".format(getpass.getuser())

    
    elif os.name == "posix":
        try:
            os.mkdir("/home/{}/D3ViLDownloader/".format(getpass.getuser()))
            path = "/home/{}/D3ViLDownloader/".format(getpass.getuser())
        except FileExistsError:
            path = "/home/{}/D3ViLDownloader/".format(getpass.getuser())
            

    return path


def helper():
    """
=====================================================================================
============================= D3ViLFileTransfer v1.0 ================================
===================    A simple tool for transfering files     ======================
=================== with socket programming in python language ======================
=================== I hope use it and enjoy it and learn it xD ======================
=================================== Dr.D3ViLaM ======================================
====================================================================================="""
