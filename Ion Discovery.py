####Modules
###Modules that are used in this file
import random

####Variables

##Player values
#These are variables that pertain to the player's "avatar" in the game
maxHealth = 100
maxEnergy = 100
health = 100
energy = 100



##Commands
#A list of commands that the player can use
commands = {"help" : "Gives a list of discovered commands the player can use", "desription" : "gives a description of the room", "inventory" : "Shows the players inventory", "discover" : "Allows the player to discover new commands"}


##Inventory
#The player's inventory, for items they collect throughout the game
inventory = {}



##Loop booleans
#These are the varaibles that are used for loops
main = True


##Main booleans
#These are the booleans used in the main loop
initialLine = True
panel = False
gearJam = False
doorLock = True
endGame = False


##Discovery booleans
#These are the booleans used in the discovery mechanic

#Inspect command
inspectDiscovered = False

#Take command
takeDiscovered = False
takeHint = False

#Push command
pushDiscovered = False
pushHint = False

#Combine Command
combineDiscovered = False
combineHint = False


##Take booleans
#These are booleans used in the take command
stunGun = False
bearingsInv = False





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
    


##Discover
#Discover 'applications' (commands) that the player can use
def discover():
    global action
    global name
    global inspectDiscovered
    global takeDiscovered
    global takeHint
    global pushDiscovered
    global pushHint
    global combineDiscovered
    global combineHint


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
        print (">> HINT: To obtain that which you desire with your own hands")


    #Push command hint
    if pushDiscovered == False and pushHint == True:
        print (">> HINT: To force something away from you")


    #Combine command hint
    if combineDiscovered == False and combineHint == True:
        print (">> HINT: To merge things for a singular purpose")

            
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
            commands["take"] = "Take an item"

            #Tells player a new command was discovered and an explanation of what it does
            print (">>> NEW APPLICATION DISCOVERED.")
            print (">>> THE TAKE APPLICATION CAN BE USED TO PICK UP AND COLLECT ITEMS.")


        #For discovering the push command
        elif guess == "push" and pushDiscovered == False:

            pushDiscovered = True

            #Adds command to "commands" dictionary
            commands["push"] = "Push an object"

            #Tells player a new command was discovered and an explanation of what it does
            print (">>> NEW APPLICATION DISCOVERED.")
            print (">>> THE PUSH APPLICATION CAN BE USED TO PUSH OBJECTS IN THE ENVIRONMENT.")


        #For discovering the combine command
        elif guess == "combine" and combineDiscovered == False:

            combineDiscovered = True

            #Adds command to "commands" dictionary
            commands["combine"] = "Combine an object from your inventory with something else"

            #Tells player a new command was discovered and an explanation of what it does
            print (">>> NEW APPLICATION DISCOVERED.")
            print (">>> THE COMBINE APPLICATION CAN BE USED TO COMBINE AN OBJECT IN YOUR INVENTORY WITH SOMETHING ELSE.")
            


        #If the search term doesn't match any discoverable command 
        else:
            print (">>> THIS IS NOT A VALID SEARCH TERM. NO NEW APPLICATIONS DISCOVERED.")
            print (">>> PLEASE TRY AGAIN.")
            

            

        

        


##Inspect
#Allows the player to inspect specific parts of the area
def inspect():
    global action
    global stunGun
    global pushHint
    global takeHint
    global combineHint
    global gearJam

    
    print (">>> INSPECT APPLICATION INITIALISED")
    print (">>> TYPE CANCEL TO EXIT THE APPLICATION")
        
    while action == "inspect":

        
        inspection = input("What do you want to inspect?").lower()

        #The player inspects the door
        if inspection == "door":
            print ("Taking a closer look at the metal door, you see it has no handle. Its smooth to the touch, and a thick layer of dust covers it suggesting it hasen't been used in a long while.")

           
        #The player inspects the workbench
        elif inspection == "bench":
            print ("You look over the bench, shifting through the dust and various junk on it. Among the junk you find a few things of interest.")

            #Removes stun gun after being taken
            if stunGun == False:
                print ("You find a stun gun. Its a rectangular object with two prongs sticking out one of the shorter sides and the image of a lightning bolt painted on it. Theres a button on the one of the long side, that causes sparks of electricity to jump out from the prongs.")

            print ("There a large number of steel ball bearings in a massive bag next to the bench.")

            if panel == False:
                print ("You also find a button on the bottom side of the desk.")

            if takeHint == False:
                #Unlocks take command hint
                print ("Seeing the items, you feel a thought pushing through from the back of your mind as your hand hovers over the bench. You try to make sense of it, but something feels missing")
                print (">>> DISCOVERY ALERT. NEW APPLICATION HINT DISCOVERED. OPEN DISCOVERY TO VIEW AND ATTEMPT DOWNLOAD OF NEW APPLICATION")
                takeHint = True
            

            

            
        #If the player inspects themselves
        elif inspection == "self":
            print ("Looking yourself over, you seem to be wearing a survival suit of some kind. Your wearing an entirely yellow suit with no seems and black gloves attached to the forearms. The suit reaches up past your neck and covers your entire head, apart from your face.")


        #The player inspects the stun gun
        elif inspection == "stun gun":
            print ("Its a rectangular object with two prongs sticking out one of the shorter sides and the image of a lightning bolt painted on it. Theres a button on the one of the long side, that causes sparks of electricity to jump out from the prongs.")

            
            
            
        #The player inspects the button
        elif inspection == "button":
            print ("Theres a small red button on the underside of the workbench. You get a sudden urge to... do something to it, but don't know how.")
            

            if pushHint == False:
                #Unlocks push command hint
                print (">>> DISCOVERY ALERT. NEW APPLICATION HINT DISCOVERED. OPEN DISCOVERY TO VIEW AND ATTEMPT DOWNLOAD OF NEW APPLICATION")
                pushHint = True


        #The player inspects the newly opened panel
        elif inspection == "panel" and panel == True:

            print ("You take a look at the panel. The inside is lined by a yellow border, with the word 'MAINTENANCE' in big black letters along the top border.")

            if gearJam == False:
                print ("Three large gears turn at the bottom of the panel, continously opening and closing a smaller panel in the top section.")

            elif gearJam == True:
                print ("Three large gears, pushing against and jammed by numerous ball bearings at the bottom of the panel, used to continously open and clos a smaller panel in the top section.")

            print ("Inside the smaller panel, you see a glowing blue tube with the words 'ELECTRICAL RELEASE' labeled under it")
            
            if combineHint == False:
                #Unlocks combine command
                print ("Looking over the panel, your hand is drawn to the pouches in your suit. You feel like you need to use something on the panel, but you don't know how or what.")
                print (">>> DISCOVERY ALERT. NEW APPLICATION HINT DISCOVERED. OPEN DISCOVERY TO VIEW AND ATTEMPT DOWNLOAD OF NEW APPLICATION")
                combineHint = True
        

        #Lets the player exit the command
        elif inspection == "cancel":
            action = "idle"
            

        else:
            print ("This is not a valid subject for inspection")




##Take
#Allows the player to take/pick up an object
def take():
    global action
    global stunGun
    global bearingsInv
    
    

    print (">>> TAKE APPLICATION INITIALISED")
    print (">>> TYPE CANCEL TO EXIT THE APPLICATION")
    
    while action == "take":

        obtain = input ("What would you like to take?").lower()

        #Player takes the stun gun
        if obtain == "stun gun" and stunGun == False:

            print ("You take the stun gun")

            stunGun = True

            inventory["Stun Gun"] = 1

        #The player takes some ball bearings
        elif obtain == "ball bearings":

            #Creates ball bearing entry in inventory dictionary if not already made
            if bearingsInv == False:
                inventory ["Ball Bearings"] = 0
                bearingsInv = True

            #Player can only take more ball bearings if they have room
            if inventory["Ball Bearings"] <= 100:
                inventory["Ball Bearings"] += random.randint (10, 20)

                print ("You pick up a number of ball bearings")
                
            else:
                print ("Your already carrying too many ball bearings")
            

        elif obtain == "cancel":
            action = "idle"

        else:

            print ("This isn't something you can take")


##Push
#Allows players to "push" objects (for various results)
def push():
    global action
    global panel
    global doorLock
    
    

    print (">>> PUSH APPLICATION INITIALISED")
    print (">>> TYPE CANCEL TO EXIT THE APPLICATION")
    
    while action == "push":

        force = input ("What would you like to push?").lower()

        #Player pushes button
        if force == "button" and panel == False:

            #Reveals door panel
            print ("You press the button on the underside of the bench, and a small panel you previously couldn't see next to the door opens. Soon after, the button retracts back into the bench")
            panel = True

        #Open door and end game
        elif doorLock == False and force == "door":

            action = "END OF GAME"

           


        elif force == "cancel":
            action = "idle"


        else:

            print ("You can't work out how to push this")



#Combine
#Allows the player to combine an object in their inventory with something else
def combine():
    global action
    global panel
    global gearJam
    global doorLock
     

    print (">>> COMBINE APPLICATION INITIALISED")
    print (">>> TYPE CANCEL TO EXIT THE APPLICATION")
    
    while action == "combine":

        #Initial object to combine
        combine1 = input ("Pick something from your inventory that you want to combine.").lower()

        #Combine ball bearing
        if combine1 == "ball bearings":

            combine2 = input ("What do you want to combine this with?")
            
            #With panel gears
            if combine2 == "gears" and inventory["Ball Bearings"] >= 25:
                inventory["Ball Bearings"] -= 25

                print ("You drop some ball bearings into the gears. They get stuck between them, and the gears become jammed leaving the top panel permenently open")

                gearJam = True

            #Not enough ball bearings
            elif combine2 == "gears" and inventory["Ball Bearings"] < 25:

                inventory["Ball Bearings"] = 0

                print ("You drop all your ball bearings, and the gears jam for a moment. However, they soon pop the ball bearings out and begin to move again. You need more ball bearings to do this")

            else:
                print ("These cannot be combined")
            
        #Combine stun gun
        elif combine1 == "stun gun":

            combine2 = input ("What do you want to combine this with?")

            #With electrical tube
            if combine2 == "tube" and gearJam == True:
                
                print ("Sparks fly from the stun gun as you press the button on the side, and shove it into the glowing blue tube. As you do, the tube stops glowing for a second and the a large crashing sound can be heard from the metal door")
                print ("The tube eventually regains its glow, but the door seems to have moved slightly with a small crack at the end of the doorframe allowing light of somekind through.")

                doorLock = False
                
            #Not enough ball bearings
            elif combine2 == "tube" and gearJam == False:

                print ("You try to use the stun gun on the tube, but the panel door keeps closing before you can reach it.")

            else:
                print ("These cannot be combined")
                    


        elif combine1 == "cancel":
            action = "idle"


        else:

            print ("You cannot combine this with anything")


        









####Introduction
##Introduction text
print(">>> INITIALISING. " + name.upper() +".exe. 20%. 40%. 60%. 80%. 99%. INITIALISATION COMPLETE.")
print(">>> UPLOADING HIGHER FUNCTION APPLICATIONS. 20%. 40%. 50%^&*$(&£*( ERROR. UPLOAD UNSUCCESSFUL. SOME HIGHER FUNCTIONS MAY BE UNAVAILABLE TO SUBJECT.")
print(">>> USE OF DISCOVERY APPLICATION SUGGESTED TO GAIN UNAVAILABLE HIGHER FUNTION APPLICATIONS.")
print(">>> UPLOADING MISSION BRIEF. 20%. 40%. 30%^&$*$£^$ ((_ ((£*&&* ERROR. UPLOAD UNSUCCESSFUL. ATEMPTING TO SHUT DOWN SYSTEM.")
print(">>> SYSTEM SHUTDOWN UNSUCCESSFUL. ADVISE MANAGEMENT INTERVENTION.")
print(">>> \n" * 10)
print("You awaken...")



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


        action = "idle"
        
    #This is what every action will default back to
    elif action == "idle" and endGame == False:
        action = input("What will you do?").lower()


    #This accesses the 'discover' command, which allows the player to discover new commands for them to use
    elif action == "discover":
        discover()

    #This accesses the inspect command
    elif action == "inspect" and inspectDiscovered == True:
        inspect()


    #This accesses the take command
    elif action == "take" and takeDiscovered == True:
        take()


    #This accesses the push command
    elif action == "push" and pushDiscovered == True:
        push()

    #This accesses the combine command
    elif action == "combine" and combineDiscovered == True:
        combine()

    
        


        
        
        
        
    #This gives a description of the room, including changes.
    elif action == "description":
        print("Your in a workshop of some kind. At the south wall is a metal large bench, various tools and materials strewn about it. There is a large metal door in the north wall.")

        if panel == True:
            print ("Next to the door is an opened panel. The inside is lined by a yellow border, with the word 'MAINTENANCE' in big black letters along the top border.")

        action = "idle"

    #Ends game
    elif action == "END OF GAME":
        print ("As you push on the door, it opens and light shines upon you. You remove your gloves, revealing your metallic yet organic skin beneath your suit.")
        print ("You step through the door and embark out to explore the world, as an android freed from their programming.")
        print ("THE END")

        endGame = True
        action = "idle"

    #Stops program without exiting program
    elif action == "idle" and endGame == True:
        pass


        
        


    else:
        action = input("That is not a valid action. Try again")
        

    
        



    
        
