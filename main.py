import pathlib
from utils import *

if __name__ == '__main__':
    mypath = pathlib.Path.home() / 'Desktop'
    createFolders(mypath)
    moveFiles(mypath)