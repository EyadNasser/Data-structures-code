class rivalpunk:

  
  
  ''' 
  A object that holds the rivals stats
  
  Attributes
    ----------
   name: str
      The name you picked for your rival
    personality: str
      The personality you picked for your rival
    age: int
      The age you picked for your rival
    gender: int
      The gender you picked for your rival
    Humanity: int
      The humanity level you picked for your rival
    Faction: str
      The Faction you picked for your rival
    Cybernetics: int
    The number of implants you picked for your rival

    Methods
    -------
    
    __str__() -> str
	    Prints the parameters for the rivals stats to the console

    Sanity() -> int
	    Prints the value for the rivals sanity stat
     
  '''
  def __init__(self, name, level , health, humanity, faction, cybernetics):
    '''
    constructor to build a character object
    Parameters
    ----------
    name: str
      The name of your rival
    level: int
      The rivals level
    Health: int
      The rivals health
    Humanity: int
      The rivals humanity level
    Faction: str
      The rivals Faction
    Cybernetics: int
    The number of implants the rival has
    
    '''
    self.name = name
    self.level = int(level)
    self.health = int(health)
    self.humanity = int(humanity)
    self.faction = faction
    self.cybernetics = int(cybernetics)
### add a max int of 7 to cybernetics
  def __str__(user):

    
    """
    
returns

-------

Parameters for rivals stats as string
""" 
    return " Rival STATS" + "nName:" + str(user.name) + "\nLevel:" + str(user.level) + "\nHealth:" + str(user.health) + "\nHumanity:" + str(user.humanity) + "\nFaction:" + str(user.faction) + "\n # of Cybernetics:" + str(user.cybernetics) + "\nSanity:" + str(user.sanity())
   
  def sanity(user):
    return user.humanity % 7
"""
returns

-------

Sanity value as an integer
"""