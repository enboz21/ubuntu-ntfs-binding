#!/usr/bin/env python3
import os

# Get the username of the currently logged-in user
user = os.getlogin()

# Set the path where the connection files will be created
path = f"/media/{user}/"

def list_files(index):
    print("Existing file names")
    # Display existing file names to the user
    files = os.listdir(path)
    for file in files:
        index += 1
        print(f"{index}. {file}")
    return index

s = str
continue_loop = True
while continue_loop:
    # Variable 'index' is used to prevent selecting excessively high values
    index = 0
    index = list_files(index)
    print('Press "y" to create a new file')
    s = input()
    # Check if the input value is a number
    if s.isdigit():
        # If the input value is a number, check if it is less than or equal to the index and greater than 0
        if int(s) <= index and int(s) > 0:
            continue_loop = False
    # If the input value is not a number, check if it's for creating a file
    elif s == "y":
        print("File name")
        # Request the file name
        name = input()
        # Create the file
        os.chdir(path)
        os.system(f"sudo -S mkdir {name}")

# List files again to select one
files = os.listdir(path)
# Select a file from the list
selected_file = files[int(s) - 1]
# Get the port information for the drive
print("Drive port information")
drive_port = input()
# Prompt for the password and mount the drive with the connection code
os.system(f"sudo -S mount -t ntfs-3g /dev/{drive_port} /media/{user}/{selected_file}")
