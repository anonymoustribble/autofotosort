# autofotosort
Lightweight Python script to sort pictures into a year/month directory system

<b>How to use:</b>

1. Download afs.py, or clone the Git repository onto your disk.
2. Ensure you have Python installed on your system. It is avaliable at www.python.org, or through apt-get on Linux.
3. AFS will ask for a working directory. If you will be repeatedly running AFS in the same directory, you can set <code>DIRECTORY_OVERRIDE</code> to skip this step on program start.
4. AFS utilizes a file's EXIF Last Modified field to sort the image into the correct directory. 
5. AFS will create a folder for every year that is detected, and 12 folders within that folder corresponding to months. It will then sort anything in its working directory into these folders.

<br>

This is mainly a personal project, written for a specific usecase. If you have suggestions, or catch a bug (or two, or three), please report it.

<br>

You are free to use this program for your own use, and branch/fork it as you like, provided you acknowledge its source.
