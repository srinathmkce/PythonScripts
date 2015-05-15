__author__ = 'user'

import os

print(os.getcwd())

saved_path = os.getcwd()
filelist = os.listdir(r"/home/user/PycharmProjects/imagePuzzle/Puzzle")
os.chdir(r"/home/user/PycharmProjects/imagePuzzle/Puzzle")
for file_name in filelist:
    #print("Old Name : " + file_name)
    print("New Name : " + file_name.translate(None,"0123456789"))
    new_name = file_name.translate(None,"0123456789")
    os.rename(file_name, new_name)

os.chdir(saved_path)
