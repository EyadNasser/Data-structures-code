class cyberpunk:

  
  ''' 
  A object that holds the character stats
  
  Attributes
    ----------
   name: str
      The name you picked for your character
    personality: str
      The personality you picked for your character
    age: int
      The age you picked for your character
    gender: int
      The gender you picked for your character
    Humanity: int
      The humanity level you picked for your character
    Faction: str
      The Faction you picked for your character
    Cybernetics: int
    The number of implants you picked for your character

    Methods
    -------
    
    __str__() -> str
	    Prints the parameters doe the charcaters stats to the console

    Sanity() -> int
	    Prints the value for the characters sanity stat
     
  '''
  def __init__(user, name, personality, age, gender, humanity, faction, cybernetics):
    '''
    constructor to build a character object
    
    Parameters
    ----------
    name: str
      The name of your character
    personality: str
      The character's personality
    age: int
      The characters age
    gender: int
      The character's gender
    Humanity: int
      The character's humanity level
    Faction: str
      The characters Faction
    Cybernetics: int
    The number of implants the character has
    
    '''
    user.name = name
    user.personality = personality
    user.age = int(age)  
    user.gender = gender
    user.humanity = int(humanity)
    user.faction = faction
    user.cybernetics = int(cybernetics)
### add a max int of 7 to cybernetics
  def __str__(user):
    return " CHARACTER STATS" + "\nName:" + str(user.name) +  "\nPersonality:" + str(user.personality) + "\nAge:" + str(user.age) + "\nGender:" + str(user.gender) + "\nHumanity:"+ str(user.humanity) +"\nFaction:" + str(user.faction) + "\n # of Cybernetics:" + str(user.cybernetics) + "\nSanity:" + str(user.sanity())
    """
returns

-------

Parameters for character stats as string
"""
  def sanity(user):
    return user.humanity % 7
    # use modulo operator to calculate post humanity
    
"""
returns

-------

Sanity value as an integer
"""
