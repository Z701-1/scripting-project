import os
import shutil
import datetime

# Asks the user for the directory containing the files
source_directory = input("Enter the path of the folder to archive: ")

# Creates a date-stamped backup folder
date_stamp = datetime.datetime.now().strftime("%Y_%m_%d")
folder_name = "backup_" + date_stamp
backup_folder = os.path.join(source_directory, folder_name)

#Makes the new folder
os.mkdir(backup_folder)

#Loops through all files and move them to the backup folder
for filename in os.listdir(source_directory):
    file_path = os.path.join(source_directory, filename)

    #Checks if it is a file since we do not want to move folders
    if os.path.isfile(file_path):
        shutil.move(file_path, backup_folder) #Removes the original files
        #shutil.copy(file_path, backup_folder) #Copies the original files
    shutil.make_archive(backup_folder, 'zip', backup_folder)
    print(f"Backing up file {filename} into:  {backup_folder}.zip")
