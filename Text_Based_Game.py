vertical = 0                    #initializing variables and lists used across multiple functions
horizontal = 0
proposed_vertical = 0
proposed_horizontal = 0
location = []
new_location = []
room = "blank"
key = ""

items1 = {'Dark Key': 1}
items_copy1 = {'Dark Key': 1}

items2 = {'Desert Key': 1}
items_copy2= {'Desert Key': 1}

items3 = {'Grass Key': 2, 'Storm Key': 2}
items_copy3 = {'Grass Key': 2, 'Storm Key': 2}

items4 = {'Enchanted Key': 1}
items_copy4 = {'Enchanted Key': 1}

items5 = {'Enchanted Red Herring': 0}
items_copy5 = {'Enchanted Red Herring': 0}

items6 = {'Frost Key': 2}
items_copy6 = {'Frost Key': 2}

items7 = {'Icy Sense of Humor': 0}
items_copy7 = {'Icy Sense of Humor': 0}

items8 = {'Castle Key': 0}
items_copy8 = {'Castle Key': 0}



items = {}
items_copy = {}

#/**********************************************************/
#/***              Player Movement Section               ***/
#/**********************************************************/



def run():                                                                                                                      #Function that starts the game
    print ('Do you wish to move your character? You are currently located at location : [%d, %d]' %(vertical, horizontal))      #Tells the player where they are located
    print ('Press 1 if yes. Press 2 if no.')
    decision = int(input())                                                                       #User input that will determine if the player moves or not.
    while (decision == 1):                                                                        #Run movement function if user input is 1.
        movement()
    else:
        print ('You have stopped moving.')
        exit()                                                                                    #Exit game if choice is 2


def back_up():
    global horizontal
    global vertical
    global inventory_copy
    global key
    if key not in inventory_copy:                                           #If key variable does not match any items in the copy of the user's inventory list
            print('Sorry, you need the %s to enter this room.' % key)       #Entry to that room denied
            movement()                                                      #Re-run movement function
    else:                                                                   #If it does match an item in the copy of the inventory list
        print('You passed through to the next area.')                       #Enter room
        horizontal = proposed_horizontal                                    #Horizontal location updates
        vertical = proposed_vertical                                        #Vertical location updates
        map_view()                                                          #Run map_view() function

def map_view():
    global location
    print('You are currently located here on the map: ')
    for sub in location:
            new_sub = []
            for item in sub:
                new_sub.append(item)
            print(" ".join(new_sub))



def map():                                      #Function that shows the user where they are located on the map.
    global location
    global new_location
    global room
    global key

    if proposed_horizontal == -1 and proposed_vertical == -1:               #If the player wants to move to this location
        location = [['O', 'O', 'O'], ['O', 'O', 'O'], ['X', 'O', 'O']]      #List of the location
        room = 'first'                                                      #Name of the room they want to enter
        key = 'Castle Key'                                                  #Key they will need to enter room
        back_up()                                                           #Run backup() function


    elif proposed_horizontal == 0 and proposed_vertical == -1:              #Repeat for next room
        location = [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'X', 'O']]
        room = 'second'
        key = 'Castle Key'
        back_up()

    elif proposed_horizontal == 1 and proposed_vertical == -1:              #Repeat
        location = [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'X']]
        room = 'third'
        key = 'Castle Key'
        back_up()

    if proposed_horizontal == -1 and proposed_vertical == 0:                #Repeat
        location = [['O', 'O', 'O'], ['X', 'O', 'O'], ['O', 'O', 'O']]
        room = 'fourth'
        key = 'Castle Key'
        back_up()

    elif proposed_horizontal == 0 and proposed_vertical == 0:               #Repeat
        location = [['O', 'O', 'O'], ['O', 'X', 'O'], ['O', 'O', 'O']]
        room = 'fifth'
        key = ''
        back_up()

    elif proposed_horizontal == 1 and proposed_vertical == 0:               #Repeat
        location = [['O', 'O', 'O'], ['O', 'O', 'X'], ['O', 'O', 'O']]
        room = 'sixth'
        key = 'Castle Key'
        back_up()

    if proposed_horizontal == -1 and proposed_vertical == 1:                #Repeat
        location = [['X', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
        room = 'seventh'
        key = 'Castle Key'
        back_up()

    elif proposed_horizontal == 0 and proposed_vertical == 1:               #Repeat
        location = [['O', 'X', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
        room = 'eighth'
        key = ''
        back_up()

    elif proposed_horizontal == 1 and proposed_vertical == 1:               #Repeat
        location = [['O', 'O', 'X'], ['O', 'O', 'O'], ['O', 'O', 'O']]
        room = 'ninth'
        key = 'Castle Key'
        back_up()





def movement():                                         #Player movement function
    global vertical
    global horizontal
    global proposed_vertical
    global proposed_horizontal
    proposed_horizontal = horizontal
    proposed_vertical  = vertical
    print ('What direction would you like to move?')
    print ('Press 1 to move North. Press 2 to move East. Press 3 to move South. Press 4 to move West. Press 5 to stop movement')
    direction = int(input())
    if direction == 1:                                  #If User Input = 1
        if vertical < 1:                                #If the user is not already as far North as they are allowed to go
            proposed_vertical += 1                      #Add one to proposed_vertical
            map()                                       #Run the map function
            print ('After moving North, you are now at location : [%d, %d]' %(vertical, horizontal))        #State location
            duel_chance()                               #Run duel_chance() function
            enter_room()                                #Run enter_room() function
            movement()                                  #Re-Run movement() function

        else:                                           #If player is at maximum distance going North
            print ('You cannot go any further North. You are already located at location : [%d, %d]' %(vertical, horizontal))       #State location and say you can go no further in that direction
            movement()                                  #Re-run movement() function

    elif direction == 2:                                #Repeat for moving East
        if horizontal < 1:
            proposed_horizontal += 1
            map()
            print ('After moving East, you are now at location : [%d, %d]' %(vertical, horizontal))
            duel_chance()
            enter_room()
            movement()

        else:
            print ('You cannot go any further East. You are already located at location : [%d, %d]' %(vertical, horizontal))
            movement()

    elif direction == 3:                                #Repeat for moving South
        if vertical > -1:
            proposed_vertical -= 1
            map()
            print ('After moving South, you are now at location : [%d, %d]' %(vertical, horizontal))
            duel_chance()
            enter_room()
            movement()

        else:
            print ('You cannot go any further South. You are already located at location : [%d, %d]' %(vertical, horizontal))
            movement()

    elif direction == 4:                                #Repeat for moving West
        if horizontal > -1:
            proposed_horizontal -= 1
            map()
            print ('After moving West, you are now at location : [%d, %d]' %(vertical, horizontal))
            duel_chance()
            enter_room()
            movement()

        else:
            print ('You cannot go any further West. You are already located at location : [%d, %d]' %(vertical, horizontal))
            map()
            movement()

    elif direction == 5:                                #Stopping movement and ending the game
        print ('You have stopped moving.')
        exit()




#/*******************************************************************************************/

#/**********************************************************/
#/***             Character Battle Section               ***/
#/**********************************************************/

import random       #For random numbers
import time         #For pauses for dramatic effect

TLVictory = False               #Initialize Boss conditions. These will come into play later so that a player only has to defeat each of them once.
JLVictory = False
CLVictory = False


class NM():         #First character class
    def __init__(self, at, de, he, kn, du):      #Initialize character attributes
        self.at = at                                    #Player attack
        self.de = de                                    #Player defense
        self.he = he                                    #Player health
        self.kn = kn                                    #Player knowledge
        self.du = du                                    #Player duty level

class JS(NM):                                                              #Subclasses of first character class
    def __init__(self):
        super().__init__(at = 100, de = 100, he = 500, kn = 5, du = 8)     #Specific stats for each category

class RS(NM):                                                              #Next Subclass
    def __init__(self):
        super().__init__(at = 120, de = 120, he = 460, kn = 7, du = 9)

class NS(NM):                                                              #Next Subclass
    def __init__(self):
        super().__init__(at = 140, de = 120, he = 420, kn = 8, du = 10)


class LN():                                             #Second character class
    def __init__(self, at, de, he, kn, tr):      #Initialize character attributes
        self.at = at                                    #Opponent attack
        self.de = de                                    #Opponent defense
        self.he = he                                    #Opponent health
        self.kn = kn                                    #Opponent knowledge
        self.tr = tr                                    #Opponent treachery level

class TL(LN):       #Subclasses of second character class
    def __init__(self):
        super().__init__(at = 50, de = 80, he = 400, kn = 10, tr = 8)

class JL(LN):                                           #Next Subclass
    def __init__(self):
        super().__init__(at = 125, de = 120, he = 400, kn = 4, tr = 5)

class CL(LN):                                           #Next Subclass
    def __init__(self):
        super().__init__(at = 30, de = 0, he = 500, kn = 5, tr = 10)


class Monster():                        #Other enemies class
    def __init__(self, at, he, kn, tr): #Same attributes
        self.at = at
        self.he = he
        self.kn = kn
        self.tr = tr

class Grunt(Monster):                   #Subclass
    def __init__(self):
        super().__init__(at = 10, he = 100, kn = 1, tr = 1)

class Knight(Monster):                  #Next subclass
    def __init__(self):
        super().__init__(at = 50, he = 200,kn = 5, tr = 3)

class Ogre(Monster):                    #Next subclass
    def __init__(self):
        super().__init__(at = 100, he = 200,kn = 3, tr = 4)



def stat():             #Function for displaying player's stats
    print ('''Stats:
    at = {}, de = {}, he = {}, kn = {}, du = {}'''.format(player.at, player.de, player.he, player.kn, player.du).replace('.0', ''))

def opp_stat():         #Function for displaying boss opponent's stats
    print ('''Stats:
    at = {}, de = {}, he = {}, kn = {}, tr = {}'''.format(opp.at, opp.de, opp.he, opp.kn, opp.tr).replace('.0', ''))

def simple_stat():      #Function for displaying minor opponent's stats
    print ('''Stats:
    at = {} , he = {}, kn = {}, tr = {})'''.format(opp.at, opp.he, opp.kn, opp.tr).replace('.0', ''))

def char_select():      #Character selection function
    global player
    print ('Choose a character:') #Character Selection
    print( 'Press 1 for JS.')
    player = JS()       #Temporarily sets player to this character
    stat()              #Displays stats for character

    print( 'Press 2 for RS.')   #Repeat Character stats
    player = RS()
    stat()

    print( 'Press 3 for NS.')   #Repeat Character stats
    player = NS()
    stat()

    play_num = int(input())     #Character Selection
    if play_num == 1:           #If user input = 1
        player = JS()           #Player is JS()
        print ('You have chosen JS.')
    elif play_num == 2:         #If user input = 2 player is RS()
        player = RS()
        print ('You have chosen RS')
    elif play_num == 3:         #If user input = 3 player is NS()
        player = NS()
        print ('You have chosen NS')




duty_plus = 0               #Initializing variables used across several functions
treachery_plus = 0
knowledge_plus = 0
opp_knowledge_plus = 0
h_bank = 0


def duty():               #Duty Attack Bonus/Curse Function
    global duty_plus
    global player
    duty_plus = 0
    duty_rand = random.randint(1,11)        #'duty_rand' = random number between 1 and 10

    if player.du >= duty_rand:                  #If the player's duty level is higher than 'duty_rand'
        print ("You won't back down.")
        duty_plus += (player.du * random.randrange(1,6))    #'duty_plus' is increased, which means the player will later receive an attack bonus which is also random
    else:
        print ("Your duty has blinded you.")    #If the player's duty level is lower than 'duty_rand'
        duty_plus -= (player.du * random.randrange(1,4))    #'duty_plus' is decreased, which means the player will later lose attack points


def treachery():        #Treachery Attack Bonus/Curse Function
    global treachery_plus
    treachery_plus = 0
    treachery_rand = random.randint(1,11)   #'treachery_rand = random number between 1 and 10
    if opp.tr >= treachery_rand:                                #If opponent's treachery level is higher than 'treachery_rand'
        print("Your opponent has used their deceit to gain an advantage.")
        treachery_plus += (opp.tr * random.randrange(5,16))     #'treachery_plus' is increased, which means the opponent will later receive an attack bonus
    else:                                                       #If opponent's treachery level is lower than 'treachery_rand'
        print ("Your opponent has been betrayed by their own treachery.")
        treachery_plus -= (opp.tr *random.randrange(1,4))       #'treachery_plus' is decreased, which means the opponent will later lose attack points

def knowledge():        #Knowledge bonus
    global knowledge_plus
    global opp_knowledge_plus
    global player
    knowledge_plus = 0
    opp_knowledge_plus = 0
    if player.kn > opp.kn:                                                      #If player knowledge level is higher than opponent knowledge level
        print ("You are smarter than your opponent. You will take less damage for the round.")
        knowledge_plus += ((player.kn - opp.kn) * random.randint(1,8))         #'knowledge_plus' is increased by the difference in level times a random number. This value is later subtracted from the opponent's attack points
        print ("Knowledge_plus is:")
        print(knowledge_plus)
    elif opp.kn > player.kn:                                                    #If opponent knowledge level is higher than the player's
        print ("Your opponent is smarter than you. Your opponent will take less damage for the round.")
        opp_knowledge_plus += ((opp.kn - player.kn) * random.randint(1,8))     #'opp_knowledge_plus' is increased by the difference in level times a random number. This value is later subtracted from the player's attack points.
        print ("Opponent's knowledge_plus is:")
        print (opp_knowledge_plus)
    else:                                                                                       #If knowledge levels are equal
        print ("You are of equal intelligence as your opponent. No intelligence boost gained")  #No advantage given



def player_at():        #Player Attack function
    duty()        #Call duty function
    global duty_plus
    global player
    c = random.randrange(1,100)                 #'c' = random number between 1 and 100
    if c <= 10:                                                 #If 'c' <= 10
        opp.he -= (player.at + 20 + duty_plus - opp_knowledge_plus)     #Adds 20 in addition to the other bonuses earned by player and opponent to this point. Takes that much health away from opponent.
        time.sleep(1)
        print ("Critical hit.")
        time.sleep(1)
        print ('You/re opponent has {} health remaining'.format(opp.he))
    elif 10 < c < 90:                                                   #If 10 <= 'c' <= 90
        opp.he -= (player.at + duty_plus - opp_knowledge_plus)          #Adds up bonuses for player and opponent. Takes that much health away from opponent.
        time.sleep(1)
        print ('Successful hit.')
        time.sleep(1)
        print ('You/re opponent has {} health remaining'.format(opp.he))
    else:                                                               #If 'c' > 90
        time.sleep(1)
        print ('You have missed.')                                      #Attack misses. No damage done to opponent.
        time.sleep(1)
        print ('You/re opponent has {} health remaining'.format(opp.he))

def opp_at():           #Opponent Attack Function
    treachery()   #Call treachery function
    global h_bank
    global treachery_plus
    global player
    d = random.randrange(1,100)         #'d' = random number between 1 and 100
    if d <= 5:                                                              #If 'd' is <= 5
        if (opp.at + 20 + treachery_plus - knowledge_plus) >= 10:           #If opponent attack with all bonuses plus 20 >= 10
            player.he -= (opp.at + 20 + treachery_plus - knowledge_plus)    #Add 20 to opponent attack in addition to bonuses. That amount is deducted from player health
            h_bank += (opp.at + 20 + treachery_plus - knowledge_plus)       #That same amount is added to the player's health bank
            time.sleep(1)
            print ("Critical hit.")
            time.sleep(1)
            print ('You have {} health remaining'.format(player.he))
        else:                                                               #If opponent attack with all bonuses plus 20 <10
            player.he -= 10                                                 #Subtract 10 from player's health
            h_bank += 10                                                    #Add 10 to player's health bank
            time.sleep(1)
            print ("Opponent's attack is not very effective, you are much stronger than your opponent.")
            time.sleep(1)
            print ('You have {} health remaining'.format(player.he))
    elif 5 < d <= 80:                                                       #If 5 < 'd' <= 80
        if (opp.at + treachery_plus - knowledge_plus) >= 10:                #If opponent's attack plus bonuses >= 10
            player.he -= (opp.at + treachery_plus - knowledge_plus)         #Add up opponent's attack plus bonuses. Subtract that amount from player's health
            h_bank += (opp.at + treachery_plus - knowledge_plus)            #Add that amount to player's health bank
            time.sleep(1)
            print ('Successful hit.')
            time.sleep(1)
            print ('You have {} health remaining'.format(player.he))
        else:                                                               #If opponent attack with all bonuses <10
            player.he -= 10                                                 #Subtract 10 from player's health
            h_bank += 10                                                    #Add 10 to player's health bank
            time.sleep(1)
            print ("Opponent's attack is not very effective, you are much stronger than your opponent.")
            time.sleep(1)
            print ('You have {} health remaining'.format(player.he))
    else:                                                                   #If 'd' > 80
        time.sleep(1)
        print ('You/re opponent has missed.')                               #Attack misses. No damage to player.
        time.sleep(1)
        print ('You have {} health remaining'.format(player.he))

def defend_heal():      #Player Heal Function
    global h_bank
    global player
    if random.randrange(1,100) <= 50:           #If random number is <= 50
        if h_bank >= player.de:                 #If player health bank is >= player defense points number
            player.he += player.de              #Player's health increases by it's defense points number
            h_bank -= player.de                 #Player's health bank decreases bby it's defense points number
            time.sleep(1)
            print ('You have healed. You now have {} health.'.format(player.he))
        elif h_bank > 0:                        #If 0 < player's health bank < player defense points number
            player.he += h_bank                 #Player's health increases by the health bank's number
            h_bank = 0                          #Player's health bank resets to zero. This way a player cannot gain more health than they originally have at the start
            time.sleep(1)
            print ('You have healed. You now have {} health.'.format(player.he))
        else:                                   #If player's health bank = 0
            player.he += 0                      #Player's health does not increase
            time.sleep(1)
            print ('You cannot heal any more. You have {} health.'.format(player.he))
    else:
        print ('Your opponent is too fast. You were unable to heal.')

def duel():         #Duel Function
    global TLVictory
    global JLVictory
    global CLVictory
    global opp
    global h_bank
    opponent = random.randint(0,1000)           #'opponent' = random number between 1 and 1000
    opp_num = 0
    if opponent <= 75:                          #If 'opponent' <= 75
        if TLVictory == False:                  #If TL() boss has not been defeated yet.
            opp = TL()                          #Opponent is now TL()
            print("Your opponent is TL")
            opp_stat()                          #Show stats
            opp_num = 1                         #Identifier to be used later after opponent is defeated
        else:                                   #If TL() boss has already been defeated
            opp = Grunt()                       #Opponent is now Grunt()
            print("Your opponent is a Grunt")
            simple_stat()                       #Show smaller opponent's stats

    elif 75 < opponent <= 150:                  #If random number is between 75 and (including) 150
        if JLVictory == False:                  #If JL() boss has not been defeated yet
            opp = JL()                          #Opponent is now JL()
            print("Your opponent is JL")
            opp_stat()                          #Show stats
            opp_num = 2                         #Identifier to be used later after opponent is defeated
        else:                                   #If JL() boss has already been defeated
            opp = Knight()                      #Opponent is now Knight()
            print("Your opponent is a Knight")
            simple_stat()                       #Show smaller opponent's stats

    elif 150 < opponent <= 225:                 #If random number is between 150 and (including) 225
        if CLVictory == False:                  #If CL() boss has not been defeated yet
            opp = CL()                          #Opponent is now CL()
            print ("Your opponent is CL")
            opp_stat()                          #Show stats
            opp_num = 3                         #Identifier to be used later after opponent is defeated
        else:                                   #If CL() boss has already been defeated
            opp = Ogre()                        #Opponent is now Ogre()
            print ("Your opponent is an Ogre")
            simple_stat()                       #Show smaller opponent's stats

    elif 225 < opponent <= 325:                 #If random number is between 225 and (including) 325
        opp = Ogre()                            #Opponent is now Ogre()
        simple_stat()                           #Show smaller opponent's stats
        print ("Your opponent is an Ogre")

    elif 325 < opponent <= 575:                 #If random number is between 325 and (including) 575
        opp = Knight()                          #Opponent is now Knight()
        simple_stat()                           #Show smaller opponent's stats
        print ("Your opponent is a Knight")

    elif opponent > 575:                        #If random number is greater than 575
        opp = Grunt()                           #Opponent is now Grunt()
        simple_stat()                           #Show smaller opponent's stats
        print ("your opponent is a Grunt")

    print("You/re opponent has arrived.")
    knowledge()                                 #Run knowledge function
    while opp.he > 0:                           #While opponent still has health points
        if player.he > 0:                       #If the player has health points
            print('Make your move. '
                  '(1) Attack'
                  '(2) Defend')
            move = int(input())                 #User input decides either attack or defend
            if move == 1:
                player_at()                     #Run player attack function
                if opp.he <= 0:                 #If opponent's health is <= 0
                    print ('Opponent has been defeated.')
                    if opp_num == 1:            #If opp_num from previous section = 1
                        TLVictory = True        #TLVictory now = True. You just defeated TL() boss and do not have to face it again.
                        player.he += h_bank     #Fully restore health for beating a boss
                        h_bank = 0              #Reset health bank to zero
                        print ("Your health has been restored.")
                    elif opp_num == 2:          #Repeat for JL() boss
                        JLVictory = True
                        player.he += h_bank
                        h_bank = 0
                        print ("Your health has been restored.")
                    elif opp_num == 3:          #Repeat for CL() boss
                        CLVictory = True
                        player.he += h_bank
                        h_bank = 0
                        print ("Your health has been restored.")
                    else:
                        print("Defeat a boss to regain health.")
                    #Add callout for function for entering room
                else:                           #If opponent still has health points
                    opp_at()                    #Run opponent attack function
            elif move == 2:                     #If user input = 2, to defend and heal
                defend_heal()                   #Run defend_heal() function
                opp_at()                        #Run opponent attack function

        else:                                   #If player has no health points remaining
            print('You lose.')
            exit()                              #Exit game. Game over


def duel_chance():                              #duel_chance() function
    chance = random.randint(0,1000)             #chance = random number between 0 and 1000
    if chance < 600:                            #If chance > 600
        duel()                                  #Run duel function



#/**************************************************************************************************/


#/**********************************************************/
#/***               Item Add_Drop Section                ***/
#/**********************************************************/


inventory = {}                      #Player inventory list
inventory_copy = {'':0}             #Copy of inventory list that changes while for loop iterates 'inventory' list. This avoids an error for modifying a list size while iterating through it. Starts with blank space to allow player to enter first room.
item_total = 0                      #Initial item total
item_weight = 0                     #Initial item weight

def add_item():                     #Function to add an item to the user's inventory
    global item_total
    global item_weight
    global items
    global items_copy
    print ('You found the following items:')
    print (items_copy)                          #displays changing dictionary
    print('Would you like to take any items? You can carry up to 3 items or 6 pounds.')
    print ('Press 1 to take. Press 2 to drop an item. Press 3 to end.')
    enter = input()                             #User input
    try:
        fake = int(enter)                       #Checks that the user input an integer
    except ValueError:                          #Throws this error response if not an integer
        print ('Sorry that is not a valid response. Please enter 1, 2, or 3.')
        add_item()                              #Re-run add_item() function

    take = int(fake)                           #Variable take = user input
    if take == 3:
        print('You chose to not pick up any items.')
        items = {}                              # Reset items to blank
        for thing in items_copy:                # Set items = items_copy
            items[thing] = items_copy[thing]
    elif take == 1:
        print ('Which object would you like to take?')
        print (items_copy)                      #Prints item list if choice = 1
        choice = str(input())                   #User types in name of item
        for word in items:                      #iterates through dictionary that does not change
            if word == choice:                  #If user input matches an item in the dictionary
                print ('You selected %s' %choice)
                if ((item_total + 1) <= 3) and ((item_weight + items[word]) <= 6):      #If the item will not put the user over their weight or item limit

                    inventory[word] = items[word]                                       #Add item to the user's inventory
                    inventory_copy[word] = items[word]                                  #Add item to the copy of the inventory list
                    print ('You now have the following in your inventory:')
                    print (inventory)                                                   #Display inventory list
                    item_total += 1                                                     #Add 1 to user's item total
                    #print (item_total)
                    item_weight += inventory[word]                                      #Add item weight to user's item weight total
                    #print (item_weight)
                    del items_copy[word]                                                #Remove item from item's found list
                    add_item()                                                          #Re-run add_item() function
                elif (item_total + 1) > 3:                                  #If the item will put the over their item limit
                    print ('You cannot pick up anymore items.')
                    drop_item()                                             #Run drop_item() function
                    add_item()                                              #Run add_item() function
                elif (item_weight + items[word]) > 6:                       #If the item will put the user over the weight limit
                    print ('That will put you over the weight limit. You cannot pick that item up.')
                    drop_item()                                             #Run drop_tem() function
                    add_item()                                              #Run add_item() function
            elif choice not in items:                               #If choice is not found in items dictionary
                print ('That is not one of the items.')
                add_item()                                          #Re-run add_item() function
    elif take == 2:                             #If user choice = 2
        drop_item()                             #Run drop_item() function
        add_item()                              #Run add_item() function
    else:                                       #If user types a number other than 1, 2, or 3.
        print ('Sorry that is not a valid response. please enter 1, 2, or 3.')
        add_item()                              #Re-run add_item() function



def drop_item():                                #Function that allows user to drop an item from their inventory list
    global item_total
    global item_weight
    print ('Would you like to drop an item? You may be able to pick up another item if you drop something.')
    print ('Press 1 to choose an item to drop. Press 2 to avoid dropping an item.')
    enter_two = input()                         #User input
    try:
        make = int(enter_two)                   #Checks that the input is an integer
    except ValueError:                          #Throws error if it is not
        print ('Sorry that is not a valid response. Please enter 1, 2, or 3.')
        drop_item()                             #Re-run drop_item() function

    drop_choice = int(make)
    if drop_choice == 1:                        #If drop choice = 1
        print ('Which item would you like to drop?')
        print (inventory)                       #Prints user inventory
        drop = str(input())                     #User input that determines which input is dropped
        for option in inventory_copy:                               #Iterates through inventory_copy list
            if option == drop:                                      #If user input = item in inventory_copy
                print('You have chosen to drop your %s' %option)
                items_copy[option] = inventory_copy[option]         #Add item to items_copy dictionary so that a user can pick that item up again later
                item_total -= 1                                     #Subtract 1 from user's item total
                item_weight -= inventory_copy[option]               #Subtract item weight from user's item weight total
                del inventory[option]                               #Remove item from user's inventory
            elif option not in inventory_copy:                      #If user input is not in inventory list
                print('That is not a valid response.')
        for each in inventory:                                      #Iterates through user's inventory list
            inventory_copy[each] = inventory[each]                  #Copies inventory list over to inventory_copy
    elif drop_choice == 2:                      #If user chooses not to drop an item
        add_item()                              #Re-run add_item() function
    else:                                       #If user types in number other than 1 or 2.
        print ('Please press 1 or 2.')
        drop_item()                             #Re-runs drop_item() function


def enter_room():                               #Function that runs as a user enters a room
    global room, items, items_copy, items1, items2, items3, items4, items5, items6, items7, items8, items_copy1, items_copy2, items_copy3, items_copy4, items_copy5, items_copy6, items_copy7, items_copy8

    print ('You have entered the %s' %room)

    if room == "Outer Gates":                                   #If room is 'specified location'
        items = {}                                              #Reset items to blank
        items_copy = {}                                         #Reset items_copy to blank
        for each in items1:                                     #Set items = items1
            items[each] = items1[each]
        for each_copy in items_copy1:                           #Set items_copy = items_copy1
            items_copy[each_copy] = items_copy1[each_copy]

        add_item()                                              #Run add_item()

        items1 = {}                                             #Reset items1 to blank
        items_copy1 = {}                                        #Reset items_copy1 to blank
        for each in items:                                      #Set items1 = items (items should be different after add_items()
            items1[each] = items[each]
        for each_copy in items_copy:                            #Set items_copy1 = items_copy
            items_copy1[each_copy] = items_copy[each_copy]

    elif room == "Watchful Town":                               #Repeat item conditions for next room
        items = {}
        items_copy = {}
        for each in items2:
            items[each] = items2[each]
        for each_copy in items_copy2:
            items_copy[each_copy] = items_copy2[each_copy]

        add_item()

        items2 = {}
        items_copy2 = {}
        for each in items:
            items2[each] = items[each]
        for each_copy in items_copy:
            items_copy2[each_copy] = items_copy[each_copy]

    elif room == "Desolate Desert":                             #Repeat item conditions for next room
        items = {}
        items_copy = {}
        for each in items3:
            items[each] = items3[each]
        for each_copy in items_copy3:
            items_copy[each_copy] = items_copy3[each_copy]

        add_item()

        items3 = {}
        items_copy3 = {}
        for each in items:
            items3[each] = items[each]
        for each_copy in items_copy:
            items_copy3[each_copy] = items_copy[each_copy]

    elif room == "Vast Grasslands":                             #Repeat item conditions for next room
        items = {}
        items_copy = {}
        for each in items4:
            items[each] = items4[each]
        for each_copy in items_copy4:
            items_copy[each_copy] = items_copy4[each_copy]

        add_item()

        items4 = {}
        items_copy4 = {}
        for each in items:
            items4[each] = items[each]
        for each_copy in items_copy:
            items_copy4[each_copy] = items_copy[each_copy]

    elif room == "Enchanted City":                              #Repeat item conditions for next room
        items = {}
        items_copy = {}
        for each in items5:
            items[each] = items5[each]
        for each_copy in items_copy5:
            items_copy[each_copy] = items_copy5[each_copy]

        add_item()

        items5 = {}
        items_copy5 = {}
        for each in items:
            items5[each] = items[each]
        for each_copy in items_copy:
            items_copy5[each_copy] = items_copy[each_copy]

    elif room == "Stormy Bay":                                  #Repeat item conditions for next room
        items = {}
        items_copy = {}
        for each in items6:
            items[each] = items6[each]
        for each_copy in items_copy6:
            items_copy[each_copy] = items_copy6[each_copy]

        add_item()

        items6 = {}
        items_copy6 = {}
        for each in items:
            items6[each] = items[each]
        for each_copy in items_copy:
            items_copy6[each_copy] = items_copy[each_copy]

    elif room == "Frozen Pass":                                 #Repeat item conditions for next room
        items = {}
        items_copy = {}
        for each in items7:
            items[each] = items7[each]
        for each_copy in items_copy7:
            items_copy[each_copy] = items_copy7[each_copy]

        add_item()

        items7 = {}
        items_copy7 = {}
        for each in items:
            items7[each] = items[each]
        for each_copy in items_copy:
            items_copy7[each_copy] = items_copy[each_copy]

    elif room == "Blackened Waste":                             #Repeat item conditions for next room
        items = {}
        items_copy = {}
        for each in items8:
            items[each] = items8[each]
        for each_copy in items_copy8:
            items_copy[each_copy] = items_copy8[each_copy]

        add_item()

        items8 = {}
        items_copy8 = {}
        for each in items:
            items8[each] = items[each]
        for each_copy in items_copy:
            items_copy8[each_copy] = items_copy[each_copy]

    else:
        print ('Congratulations! You have avoided your enemies and reached your home.')
        exit()

#add_item()



#/**************************************************************************************************/

char_select()
run()
