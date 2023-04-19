"""
AutoFotoSort (AFS)
Version: 1.45
Created: Jan 6 2023
Last Modified: Feb 22 2023
(c) 2023 anonymoustribble
"""

#IMPORT
import os
import shutil
import time

#CONSTANTS
YEAR = "2023"
VERSION = "1.45"
DIRECTORY_OVERRIDE = ""
MONTHS = ["01-Jan", "02-Feb", "03-Mar", "04-Apr", "05-May", "06-Jun", "07-Jul", "08-Aug", "09-Sep", "10-Oct", "11-Nov", "12-Dec"]

#VARIABLES
folder = ""
fileList = []
yearList = []
existingYearList = []

#START AND SETUP

def start():
    print("AutoFotoSort (AFS)")
    print("Version "+VERSION)
    print("(c) "+YEAR+" anonymoustribble\n")
    
    if DIRECTORY_OVERRIDE == "":
        return input("> Input working directory: ")
    else:
        print("> Input working directory: OVERRIDE")
        return DIRECTORY_OVERRIDE

#GET IMAGES FROM DIRECTORY
    
def getImages(folder):
    print("> locating images...")
    global fileList
    removeList = []
    os.chdir(folder)
    fileList = os.listdir()
    for file in fileList:
        folderFlag = True
        for letter in file:
            if letter == ".":
                folderFlag = False
                break
        if folderFlag == True:
            removeList.append(file)
    for file in removeList:
        fileList.remove(file)
    
    if fileList == []:
        print("> error x1: no files detected in this directory")
        time.sleep(2)
        exit()
        
    if input("> found "+str(len(fileList))+" photos. Proceed (y/n)? ") != "y":
        exit()
    

#CREATE FOLDERS FOR ORGANIZATION BY YEAR

def createFolders():
    global fileList
    global yearList
    print("> detected years...")
    
    for file in fileList:
        year = file[0:4]
        if year not in yearList:
            yearList.append(year)
            print("> "+year)

    checkFiles()

    for year in yearList:
        if year not in existingYearList:
            for month in MONTHS:
                os.makedirs(year+"/"+month)
    print("> folder structure complete")
    time.sleep(2)

#SORT PHOTOS

def sortPhotos():
    count = 0
    for file in fileList:
        count += 1
        year = file[0:4]
        monthNum = file[4:6]
        month = MONTHS[int(monthNum)-1]
        shutil.move(file, year+"/"+month)
        print("> move "+file)
        
    print("> moved "+str(count)+" files")

#CHECK FOR ERRORS AND ABORT IF FOUND

def checkFiles():
    global existingYearList
    flag = False
    error = ""
    for file in fileList:
        try:
            int(file[0:6])
        except:
            flag = True
            error = "x2: invalid file names"

    for year in yearList:
        files = os.listdir()
        if year in files:
            existingYearList.append(year)

    try:
        for file in fileList:
            if int(file[4:6]) > 12:
                flag = True
                error = "x4: "+file[4:6]+" is not a valid month"
    except:
        flag = True
        error = "x5: invalid file names"
            
    if flag == True:
        print("> error "+error)
        time.sleep(2)
        exit()
        

#MAINLOOP

def main():
    folder = start()
    getImages(folder)
    createFolders()
    sortPhotos()
    
    print("> operation complete")
    time.sleep(2)

main()
    


