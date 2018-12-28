####Variables
##Player values
#These are variables that pertain to the player's "avatar" in the game
health = 100
energy = 100
inventory = {"Placeholder" : 1, "Placeholder2" : 0, "Placeholder3" : 0}

##Commands
#A list of commands that the player can use
commands = ["help", "view", "take"]

##Loop booleans
#These are the varaibles that decide which loop to run at the moment
intro = True



####Setup
###Here is where setup at the start of the game occurs
name = ""
while name == "":
    name = input("What is your name?")
action = input("type anything to continue")


####Background
###These are things that can be done or looked at throughout the game by the player

##Previous action
#This keeps a record of the previous action to be used so that players don't lose progress while checking their inventory, etc.
while action not in ("help", "inventory", "i"):
    previousAction = action


##Help
#Printing a list of general commands that players may be able to use
while True:
    if action in ("help"):
        print(commands)
        action = previousAction


##Inventory
#Allows the player to check their inventory
while True:
    if action in ("inventory", "i"):
        print(inventory)
        action = previousAction



####Introduction
while intro:

    action = input("placeholder text").lower()

    if action in ("test"):
        print("Test")
        



    
        
