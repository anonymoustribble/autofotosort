"""
AutoFotoSort (AFS)
Version: 2
Created: Jan 6 2023
Last Modified: May 23 2023
(c) 2023 anonymoustribble
"""

#IMPORT
import time
import sorting as sort

#CONSTANTS
YEAR = "2023"
VERSION = "2"
DIRECTORY_OVERRIDE = ""
MONTHS = ("01-Jan", "02-Feb", "03-Mar", "04-Apr", "05-May", "06-Jun", "07-Jul", "08-Aug", "09-Sep", "10-Oct", "11-Nov", "12-Dec") 

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


#MAINLOOP

def main():

    #Declare variables 
    folder = ""
    fileList = [] 

    #Get working directory
    folder = start()

    #Get a list of images in directory
    fileList = sort.getImages(folder)

    #Create folder structure
    sort.createFolders(fileList, MONTHS)

    #Sort photos
    sort.sortPhotos(fileList, MONTHS)
    
    print("> operation complete")
    time.sleep(2)


main()
    


