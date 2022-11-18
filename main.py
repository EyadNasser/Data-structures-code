#-----------------------------------------------------------------------------
# Name:        CyberPunk
# Purpose:     Learning how to use classes and methods
#
# Author:      Eyad Nasser
# Created:     oct-2022
# Updated:     oct-2022
#-----------------------------------------------------------------------------
from punk import cyberpunk
from rival_punk import rivalpunk
import random

cyber_list = []

with open( "user_input.txt" , 'r') as data:
  cyber_data = data.readlines()
  
  line = cyber_data[0]
  name, personality, age, gender, humanity, faction, cybernetics = line.split(",")
  cyber_list.append(cyberpunk( name, personality, age, gender, humanity, faction,cybernetics))
    
  line = cyber_data[1]
  name, level, health, humanity, faction, cybernetics = line.split(",")
  cyber_list.append(rivalpunk(name, level, health, humanity, faction, cybernetics))


        

with open('user_output.txt', 'w') as file:
  cyberdata_string = ""
  for punk in cyber_list:
    cyberdata_string += str(punk) + "\n"
  file.write(cyberdata_string)
  print(cyberdata_string)



winner = random.sample(cyber_list, 1)
print("WINNER: " + winner[0].name)