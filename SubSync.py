__author__ = 'user'

import os
import sys
import re
import shutil
from os.path import basename

from os import path

# Function to identify the episode Number
def identifyEpisodeNumber(filename):
    return re.findall('[E,e]\d\d', filename)

# Getting Video File Directory
videoDir = input("Enter the Video File Path : ")
#print(x)

# Getting Subtitle File Directory
subDir = input("Enter the Subtitle File Path : ")
#print(y)


# checking if videoDir path exists

if os.path.isdir(videoDir) == False :
    print("Video Path Doesnt Exists")
    sys.exit();

# checking if Subtitle Pat Doesnt Exist

if os.path.isdir(subDir) == False :
    print("Subtitle Path Doesnt Exists")
    sys.exit()

# container for video and subtitle files
videoFiles = []
subFiles = []
# Grabbing all files under Video Directory

dirListing = []
index = 0
dirListing = os.listdir(videoDir)
for filename in dirListing :
    if os.path.isfile(videoDir + "/" + filename) == True:
        videoFiles.insert(index , filename)
        index = index + 1

# Grabbing all files under Subtitle Directory

dirListing = []
index = 0
dirListing = os.listdir(subDir)
for filename in dirListing :
    if os.path.isfile(subDir + "/" + filename) == True:
        subFiles.insert(index , filename)
        index = index + 1

# for each video file
for filename in videoFiles:
    episodeNumberString = identifyEpisodeNumber(filename)
    episodeNumber = episodeNumberString[0][1:]
    pattern = "[e,E]"  +  episodeNumber
    # get the filename matching Episode Number
    subCount = 0
    for sfile in subFiles:
        if re.findall(pattern, sfile):
            #print("Sfile is " , sfile)
            fname, fext = os.path.splitext(videoDir + "/" + filename)
            #print("Filename is ", fname)
            source = subDir + "/" + sfile
            #print ("Source is " , source)
            dest = fname + "_" + str(subCount) + ".srt"
            #print ("Dest is ", dest)
            subCount = subCount + 1
            shutil.copy2(source,dest)
            #os.rename(source,dest)


print("Done Successfully. Thank you !!!")


