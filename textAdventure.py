####Variables
##Player values
#These are variables that pertain to the player's "avatar" in the game
maxHealth = 100
maxEnergy = 100
health = 100
energy = 100
inventory = {"Placeholder" : 1, "Placeholder2" : 0, "Placeholder3" : 0}

##Commands
#A list of commands that the player can use
commands = {"help" : "Gives a list of commands", "inventory" : "Shows the players inventory", "status" : "Checks the players health and energy level", "inspect" : "inspect a place or item", "desription" : "gives a description of the room", "take": "take an item"}

##Loop booleans
#These are the varaibles that decide which loop to run at the moment
main = True

##Intro booleans
#These are the booleans used in the intro loop
initialLine = True


####Setup
###Here is where setup at the start of the game occurs
name = input("Enter your name.")
while name == "":
    name = input("Enter an appropriate name.")
action = "inventory"


####Background and functions
###These are things that are done or looked at throughout the game by the player

###Functions

##Help
#Printing a list of general commands that players may be able to use
def helpCommands():
    print(commands)
    global action
    action = "idle"
    


##Inventory
#Allows the player to check their inventory
def inventoryCheck():
    print("<<<   INVENTORY:   >>>")
    print(inventory)
    global action
    action = "idle"
    

##Staus
##Allows players to check their status/shows status when it changes
def status():
    print("<<<<<<<  Status  >>>>>>>>")
    print("<<<   HEALTH: %d/%d   >>>" % (health, maxHealth))
    print("<<<   ENERGY: %d/%d   >>>" % (energy, maxEnergy))
    print("\n")



####Introduction
##Introduction text
print(">>> INITIALISING. " + name.upper() +".exe. 20%. 40%. 60%. 80%. 99%. INITIALISATION COMPLETE.")
print(">>> UPLOADING MISSION BRIEF. 20%. 40%. 30%^&$*$£^$ ((_ ((£*&&* ERROR. MISSION BRIEF UPLOAD UNSUCCESSFUL. ATEMPTING TO SHUT DOWN SYSTEM.")
print(">>> SYSTEM SHUTDOWN UNSUCCESSFUL. ADVISE MANAGEMENT INTERVENTION.")
print(">>> \n" * 10)
print("You awaken...")
status()


##main gameplay loop
while main:

    #This prevents the initial line of the intro from replaying after the first time
    while initialLine:
        action = input("Sitting up, you look around the room. Your in a workshop of some kind. At the south wall is a metal large bench, various tools and materials strewn about it. There is a large metal door in the north wall.").lower()
        initialLine = False

    
    

    #This set of code calls the background functions, e.g. to check inventory, find commands, etc.
    if action == ("inventory"):
        inventoryCheck()
        

    elif action == ("help"):
        helpCommands()

    elif action == ("status"):
        status()
        action = "idle"

    elif action == "idle":
        action = input("What will you do?").lower()
        
        
        

    elif action == ("description"):
        print("Your in a workshop of some kind. At the south wall is a metal large bench, various tools and materials strewn about it. There is a large metal door in the north wall.")
        action = idle
        


    else:
        action = input("That is not a valid action. Try again")
        

    
        



    
        
