#!/bin/python3


# this will show all the files and folder inside the given directory.
import os

# uncomment if like to see in current folder
#cwd=os.path.abspath('.')

cwd='/home/myserver/Downloads'

import os
for folderName, subfolders, filenames in os.walk(cwd):

    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
    print('')
