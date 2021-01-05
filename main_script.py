# Initial Python v.3.9.1 used

import os
import time as t

# This variable will get the current location of the script, in which it has been moved to
directory=os.path.dirname(__file__)

# WARNING: DO NOT REMOVE UNLESS REAL TIME EXECUTION!
# SAMPLE DIRECTORY will be changed to ----> current_directory=directory <----for execution
current_directory=os.path.join(directory,"dummy series") # SAMPLE DIRECTORY

#=========================================USER INPUT =============================================================
# Takes the number of seasons available in the current directory to rename files accordingly
seasons=int(input("Number of Seasons in this folder: "))

# This will check if the number of seasons are more than 1
### then program should ask number of episodes in different seasons, this information will be stored in a list
no_of_files_in_directory=len(os.listdir(current_directory))
newNames=list()
if seasons>1:
    no_of_episode_per_season=[]
    for _ in range(seasons):
        no_of_episode_per_season.append(int(input("Number of episodes in Season "+str(_+1)+": ")))
   
   # Below statment will check if number of files in the directory and number of episodes provided by user are equal
    print('Verifying...')
    t.sleep(1)
    assert sum(no_of_episode_per_season)==no_of_files_in_directory, "CONFLICT: NUMBER OF FILES"
    
    # COM #12: Proceed for creating newName list with names to be renamed
    for season_number in range(seasons):
        for episode_number in range(no_of_episode_per_season[season_number]):
            newNames.append("S{0:0=2d}E{1:0=2d}".format(season_number+1,episode_number+1))

elif seasons==1:
    season=int(input("Season Number: "))
    
    # COM #12: Proceed for creating newName list with names to be renamed
    for _ in range(1,no_of_files_in_directory+1):
        newNames.append("S{:0=2d}E{:0=2d}".format(season,_))

else:
    print("Issues while naming files")


""" Available information from user: 
  @var seasons -> type int [For folder containing files of different seasons]
  @var no_of_episode_per_season -> type list [Every Element in list denotes the number of epsiode in it's (index+1) season relatively]
"""
#======================================================================================================

# Function to rename files
def nameChanger(source, newName): # Takes the old and new filenames only and rename in actual
    os.rename(os.path.join(current_directory,source),os.path.join(current_directory,newName))
#======================================================================================================
print("Checking Files...")
t.sleep(1)

#======================================================================================================
# This function traverse through the files in a serial manner in the current directory
for root, dirs, files in os.walk(current_directory):
    for filename,newName in zip(files,newNames):
        nameChanger(filename,newName)
        print(filename,'Rename =>',newName)
