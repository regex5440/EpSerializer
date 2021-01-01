# Initial Python v.3.9.1 used

import os
import time as t

# This variable will get the current location of the script, in which it has been moved to
current_directory=os.path.dirname(__file__)

# DO NOT REMOVE THE BELOW LINE TILL TESTING
dummy_series_path=os.path.join(current_directory,"dummy series")

# Takes the number of seasons available in the current directory to rename files accordingly
seasons=int(input("Number of Seasons in this folder: "))

# This will check if the number of seasons are more than 1
### then program should ask number of episodes in different seasons, this information will be stored in a list
no_of_files_in_directory=len(os.listdir(dummy_series_path))
if seasons>1:
    no_of_episode_per_season=[]
    for _ in range(seasons):
        no_of_episode_per_season.append(int(input("Number of episodes in Season "+str(_+1)+": ")))
   
    print('Verifying...')
    t.sleep(1)
    # Below statment will check if number of files in the directory and number of episodes provided by user are same
    assert sum(no_of_episode_per_season)==no_of_files_in_directory, "CONFLICT: NUMBER OF FILES"
else:
    no_of_episode_per_season=no_of_files_in_directory

""" Available information from user: 
  @var  seasons of type int
  @var  no_of_episode_per_season of type list
"""

# new name list of names as per the information provided by user
newNames=list()
for season_number in range(seasons):
    for episode_number in range(no_of_episode_per_season[season_number]):
        newNames.append("S{0:0=2d}E{1:0=2d}".format(season_number+1,episode_number+1))

def nameChanger(source, newName): # Takes the old and new filenames only and rename in actual
    os.rename(os.path.join(dummy_series_path,source),os.path.join(dummy_series_path,newName))


print("Checking Files...")
t.sleep(1)

# This function traverse through the files in a serial manner in the current directory
for root, dirs, files in os.walk(dummy_series_path):
    for filename,newName in zip(files,newNames):
        nameChanger(filename,newName)
        print(filename,'Rename =>',newName)

#ADD FEATURE TO WORK WITH SINGLE SEASONS
#test comment 2