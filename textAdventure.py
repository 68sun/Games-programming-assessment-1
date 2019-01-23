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
commands = {"help" : "Gives a list of general commands the player can use", "inventory" : "Shows the players inventory", "status" : "Checks the players health and energy level", "inspect" : "inspect a place or item", "desription" : "gives a description of the room", "take": "take an item"}


##Loop booleans
#These are the varaibles that decide which loop to run at the moment
main = True


##Main booleans
#These are the booleans used in the main loop
initialLine = True


##Discovery booleans
#These are the booleans used in the discovery mechanic
inspectDiscovered = False



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
#Allows players to check their status/shows status when it changes
def status():
    print("<<<<<<<  Status  >>>>>>>>")
    print("<<<   HEALTH: %d/%d   >>>" % (health, maxHealth))
    print("<<<   ENERGY: %d/%d   >>>" % (energy, maxEnergy))
    print("\n")


##Discover
#Discover 'applications' (commands) that the player can use
def discover():
    global action


    print (">>> DISCOVERY APPLICATION ACTIVATED.")
    print (">>> TYPE SEARCH TERMS TO ATTEMPT TO DISCOVER NEW APPLICATIONS FOR INSTALL.")
    print (">>> HINTS FOR DISCOVERING APPLICATIONS WILL APPEAR BELOW WHEN FOUND: ")

    #Hint for discovering the inspect command
    if inspectDiscovered == False:
        Print (">> HINT: To look closely at the elements of this world")

            
    while action == "discover":


        #Players guess to attempt to discover a new command
        guess = input(">>> WHAT SEARCH TERM WOULD YOU LIKE TO TRY? TYPE CANCEL TO EXIT THE DISCOVERY APPLICATION").lower()

        if guess == "cancel":
            action = "idle"

        elif guess == "inspect":
            inspectDiscovered == True

        


##Inspect
#Allows the player to inspect specific parts of the area
def inspect():
    global action
    while action == "inspect":
        
        inspection = input("What do you want to inspect?").lower()

        if inspection == "door":
            print ("Taking a closer look at the metal door, you see it has no handle. Its smooth to the touch, and a thick layer of dust covers it suggesting it hasen't been used in a long while.")

            action = "idle"

        elif inspection == "bench":
            print ("You look over the bench, shifting through the dust and various junk on it. Among the junk you find a few things of interest.")

            print ("Theres a large spanner, covered in rust and near breaking, but could be used atleast once more.")

            print ("Theres a rectangular object with two prongs sticking out one of the shorter sides and the image of a lightning bolt painted on it. Theres a button on the one of the long side, that causes sparks of electricity to jump out from the prongs.")

            print ("There a large number of steel ball bearings in a massive bag next to the bench.")

            print ("You also find a button on the bottom side of the desk.")

            action = "idle"

        elif inspection == "self":
            print ("Looking yourself over, you seem to be wearing a survival suit of some kind. Your wearing an entirely yellow suit with no seems and black gloves attached to the forearms. The suit reaches up past your neck and covers your entire head, apart from your face.")

            action = "idle"

        else:
            print ("This is not a valid subject for inspection")
    










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
        print("Sitting up, you look around the room. Your in a workshop of some kind. At the south wall is a metal bench, various tools and materials strewn about it. There is a large metal door in the north wall.")

        print("Type Help for a list of general commands you can use. These are only general commands, the other commands can be found through exploring and experimentation.")
        
        action = "idle"
        

        initialLine = False

    
    

    #This set of code calls the background functions, e.g. to check inventory, find commands, etc.
    if action == "inventory":
        inventoryCheck()
        
    elif action == "help":
        helpCommands()

    elif action == "status":
        status()
        action = "idle"
        
    #This is what every action will default back to
    elif action == "idle":
        action = input("What will you do?").lower()


    elif action == "inspect" and inspectDiscovered == True:
        inspect()
        


        
        
        
        
    #This gives a description of the room, including changes.
    elif action == "description":
        print("Your in a workshop of some kind. At the south wall is a metal large bench, various tools and materials strewn about it. There is a large metal door in the north wall.")

        action = idle
        


    else:
        action = input("That is not a valid action. Try again")
        

    
        



    
        
