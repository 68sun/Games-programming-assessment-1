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
commands = ["help", "inventory", "status", "view", "take"]

##Loop booleans
#These are the varaibles that decide which loop to run at the moment
intro = True

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
##Previous action
#This keeps a record of the previous action to be used so that players don't lose progress while checking their inventory, etc.
def previousAction():
    global previous
    previous = action


##Help
#Printing a list of general commands that players may be able to use
def helpCommands():
    print(commands)
    global action
    action = previous


##Inventory
#Allows the player to check their inventory
def inventoryCheck():
    print("<<<   INVENTORY:   >>>")
    print(inventory)
    global action
    action = previous

##Staus
##Allows players to check their status/shows status when it changes
def status():
    print("<<<   HEALTH: %d/%d   >>>" % (health, maxHealth))
    print("<<<   ENERGY: %d/%d   >>>" % (energy, maxEnergy))



####Introduction
##Introduction text
print(">>> INITIALISING. " + name.upper() +".exe. 20%. 40%. 60%. 80%. 99%. INITIALISATION COMPLETE.")
print(">>> UPLOADING MISSION BRIEF. 20%. 40%. 30%^&$*$£^$ ((_ ((£*&&* ERROR. MISSION BRIEF UPLOAD UNSUCCESSFUL. ATEMPTING TO SHUT DOWN SYSTEM.")
print(">>> SYSTEM SHUTDOWN UNSUCCESSFUL. ADVISE MANAGEMENT INTERVENTION.")
print(">>> \n" * 10)
print("You awaken...")
status()


##intro gameplay loop
while intro:

    #This prevents the initial line of the intro from replaying after the first time
    while initialLine:
        action = input("placeholder text").lower()
        initialLine = False

    
    

    #This set of code calls the background functions, e.g. to check inventory, find commands, etc.
    if action == ("inventory"):
        inventoryCheck()

    elif action == ("help"):
        helpCommands()

    elif action == ("status"):
        status()
        action = previous
        

    elif action == ("test"):
        print("Test")
        #This saves the previous action entered by the player for use when certain funtions are used
        previousAction()
        action = input("What will you do?").lower()
        


    else:
        action = input("That is not a valid action. Try again")
        

    
        



    
        
