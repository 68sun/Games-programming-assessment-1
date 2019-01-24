####Variables

##Player values
#These are variables that pertain to the player's "avatar" in the game
maxHealth = 100
maxEnergy = 100
health = 100
energy = 100



##Commands
#A list of commands that the player can use
commands = {"help" : "Gives a list of discovered commands the player can use", "desription" : "gives a description of the room", "inventory" : "Shows the players inventory", "status" : "Checks the players health and energy level", "discover" : "Allows the player to discover new commands"}


##Inventory
#The player's inventory, for items they collect throughout the game
inventory = {}



##Loop booleans
#These are the varaibles that decide which loop to run at the moment
main = True


##Main booleans
#These are the booleans used in the main loop
initialLine = True


##Discovery booleans
#These are the booleans used in the discovery mechanic

#Inspect command
inspectDiscovered = False

#Take command
takeDiscovered = False
takeHint = False


##Take booleans
#These are booleans used in the take command
stunGun = False



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
    global name
    global inspectDiscovered
    global takeDiscovered
    global takeHint


    print (">>> DISCOVERY APPLICATION ACTIVATED.")
    print (">>> DISCOVERY CAN BE USED TO OBTAIN HIGHER FUNCTION APPLICATIONS NOT CURRENTLY INSTALLED IN SUBJECT " + name.upper())
    print (">>> TYPE SEARCH TERMS TO ATTEMPT TO DISCOVER NEW APPLICATIONS FOR INSTALL.")
    print (">>> HINTS FOR DISCOVERING APPLICATIONS WILL APPEAR BELOW WHEN FOUND: ")

    #Hint for discovering the inspect command
    #Inspect command hint
    if inspectDiscovered == False:
        print (">> HINT: To look closely at the elements of this world")

    #Take command hint
    if takeDiscovered == False and takeHint == True:
        print (">> HINT: To obtain that which you desire")

            
    while action == "discover":


        #Players guess to attempt to discover a new command
        guess = input(">>> WHAT SEARCH TERM WOULD YOU LIKE TO TRY? TYPE CANCEL TO EXIT THE DISCOVERY APPLICATION").lower()


        #Allows the player to exit discover mode
        if guess == "cancel":
            action = "idle"


        #For discovering the inspect command
        elif guess == "inspect" and inspectDiscovered == False:
            
            inspectDiscovered = True
            
            #Adds command to "commands" dictionary
            commands["inspect"] = "inspect a place or item"

            #Tells player a new command was discovered and an explanation of what it does
            print (">>> NEW APPLICATION DISCOVERED.")
            print (">>> THE INSPECT APPLICATION CAN BE USED TO INVESTIGATE SPECIFIC AREAS OR OBJECTS.")


        #For discovering the take command
        elif guess == "take" and takeDiscovered == False:

            takeDiscovered = True

            #Adds command to "commands" dictionary
            commands["take"] = "take an item"

            #Tells player a new command was discovered and an explanation of what it does
            print (">>> NEW APPLICATION DISCOVERED.")
            print (">>> THE TAKE APPLICATION CAN BE USED TO PICK UP AND COLLECT ITEMS.")


        #If the search term doesn't match any discoverable command 
        else:
            print (">>> THIS IS NOT A VALID SEARCH TERM. NO NEW APPLICATIONS DISCOVERED.")
            print (">>> PLEASE TRY AGAIN.")
            

            

        

        


##Inspect
#Allows the player to inspect specific parts of the area
def inspect():
    global action
    global stunGun

    
    print (">>> INSPECT APPLICATION INITIALISED")
    print (">>> TYPE CANCEL TO EXIT THE APPLICATION")
        
    while action == "inspect":

        
        inspection = input("What do you want to inspect?").lower()

        if inspection == "door":
            print ("Taking a closer look at the metal door, you see it has no handle. Its smooth to the touch, and a thick layer of dust covers it suggesting it hasen't been used in a long while.")

           

        elif inspection == "bench":
            print ("You look over the bench, shifting through the dust and various junk on it. Among the junk you find a few things of interest.")

            if stunGun == False:
                print ("You find a stun gun. Its a rectangular object with two prongs sticking out one of the shorter sides and the image of a lightning bolt painted on it. Theres a button on the one of the long side, that causes sparks of electricity to jump out from the prongs.")

            print ("There a large number of steel ball bearings in a massive bag next to the bench.")

            print ("You also find a button on the bottom side of the desk.")

            

        elif inspection == "self":
            print ("Looking yourself over, you seem to be wearing a survival suit of some kind. Your wearing an entirely yellow suit with no seems and black gloves attached to the forearms. The suit reaches up past your neck and covers your entire head, apart from your face.")

            



        elif inspection == "cancel":
            action = "idle"
            

        else:
            print ("This is not a valid subject for inspection")




##Take
#Allows the player to take/pick up an object
def take():
    global action
    global stunGun
    
    

    print (">>> TAKE APPLICATION INITIALISED")
    print (">>> TYPE CANCEL TO EXIT THE APPLICATION")
    
    while action == "take":

        obtain = input ("What would you like to take?").lower()

        if obtain == "stun gun" and stunGun == False:

            print ("You take the stun gun")

            stunGun = True

            inventory["Stun Gun"] = 1



        elif obtain == "cancel":
            action = "idle"

        else:

            print ("This isn't something you can take")
            


        









####Introduction
##Introduction text
print(">>> INITIALISING. " + name.upper() +".exe. 20%. 40%. 60%. 80%. 99%. INITIALISATION COMPLETE.")
print(">>> UPLOADING HIGHER FUNCTION APPLICATIONS. 20%. 40%. 50%^&*$(&£*( ERROR. UPLOAD UNSUCCESSFUL. SOME HIGHER FUNCTIONS MAY BE UNAVAILABLE TO SUBJECT.")
print(">>> USE OF DISCOVERY APPLICATION SUGGESTED TO GAIN UNAVAILABLE HIGHER FUNTION APPLICATIONS.")
print(">>> UPLOADING MISSION BRIEF. 20%. 40%. 30%^&$*$£^$ ((_ ((£*&&* ERROR. UPLOAD UNSUCCESSFUL. ATEMPTING TO SHUT DOWN SYSTEM.")
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


    #This accesses the 'discover' command, which allows the player to discover new commands for them to use
    elif action == "discover":
        discover()


    elif action == "inspect" and inspectDiscovered == True:
        inspect()


    elif action == "take" and takeDiscovered == True:
        take()

    
        


        
        
        
        
    #This gives a description of the room, including changes.
    elif action == "description":
        print("Your in a workshop of some kind. At the south wall is a metal large bench, various tools and materials strewn about it. There is a large metal door in the north wall.")

        action = idle
        


    else:
        action = input("That is not a valid action. Try again")
        

    
        



    
        
