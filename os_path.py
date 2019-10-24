#!/bin/python3

import os

print(" printing the current directory......\n")
# this will print the current worrking directory: COOL
cwd= os.path.abspath(".")
print(cwd)

print(" lets play more.... enter 'yes' if like to" )
inp=input('\n::::::::::::')

if inp=='yes':
    current_folder_name = os.path.basename(cwd)
    print("current folder name:",current_folder_name
            )
    print("\n and the directory is",os.path.dirname(cwd))


    print("lets make a list out of it\n")
    #spliting the path and making a list out of it
    path_list=cwd.split(os.path.sep)
    print(path_list
            )
else:
    print('bye')

arg=input("\nLike to check the file size: ")

if arg=='yes':
    print("Calculating the size.....")
    print(os.path.getsize(cwd))
else:
    print("okj")
    

