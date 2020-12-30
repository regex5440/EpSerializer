# Initial Python v.3.9.1 used

import os

# This variable will get the current location of the script, in which it has been moved to
current_directory=os.path.dirname(__file__)

# DO NOT REMOVE THE BELOW LINE TILL TESTING
dummy_series_path=os.path.join(current_directory,"dummy series")

# Takes the number of seasons available in the current directory to rename files accordingly
season_number=int(input("Number of Seasons in this folder: "))

# This will check if the number of seasons are more than 1
### then program should ask number of episodes in different seasons, this information will be stored in a list
if season_number>1:
    no_of_episode_per_season=[]
    for _ in range(season_number):
        no_of_episode_per_season.append(int(input("Number of episodes in Season"+str(_+1)+": ")))
    
    # Below statment will check if number of files in the directory and number of episodes provided by user are same
    assert sum(no_of_episode_per_season)==len(os.listdir(dummy_series_path)), "CONFLICT: NUMBER OF FILES"

""" Available information from user: 
  @var  season_number of type int
  @var  no_of_episode of type list
"""


# This function traverse through the files in a serial manner in the current directory
for root, dirs, files in os.walk(dummy_series_path):
    for filename in files:
        """NEW CODE SHOULD BE HERE THAT RENAME FILES ACCORDING TO NUMBER OF EPISODES AND NUMBER OF SEASONS"""