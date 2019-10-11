import random
import time

def displayIntro():
    print('''You are currently on a adventure to find the perfect pancake mix. You have arrived between two islands. On one island, you see the Aunt Jemima pancake castle.
on the other island, you see the Great Value pancake mountain on the island of Walmart.''')
    print()

def chooseArea():
    global area
    area = ' '
    while area != '1' and area != '2' :
        print('Which island will you choose? Great Value pancake mountain(1) or Aunt Jemima pancake castle(2)? ')
        area = input()

    return area


def checkArea( chosenArea ):
    global area
    print("You approach the shore.... ")
    time.sleep(2)
    print("It is warm and bright")
    time.sleep(2)
    print("You hear someone coming, and she...")
    print()
    time.sleep(2)


    friendlyArea = random.randint(1, 2)
    print ('friendlyArea')

    if chosenArea == str(friendlyArea) :
         print ("is Aunt Jemima")
    else:
         print ("is Walmart")

def chooseAppliance():
    global appliance
    appliance = ' '
    while appliance != 'fork' and appliance != 'knife'
    print ("Which appliance do you want to fend off enemies with? A fork, or a knife?")
    appliance = input()

        
def checkAppliance( chosenAppliance):
    global appliance
    print("You walk down the tunnel")
    time.sleep(2)
    print("It is wet and gloomy")
    time.sleep(2)
    print("You hear someone coming, and...")
    print()
    time.sleep(2)

    friendlyAppliance = random.randint (fork, knife)

    if chosenAppliance == str(friendlyAppliance):
        print ("You stabbed her to death")
    else:
        print ("You stabbed her to death")

def choosePath ():
    global path
    path = ' '
    while path != 'right' and path != 'left'
    print ("Which path do you want to take? Right or left?")
    path = input()


def checkPath( chosenPath):
    global path
    print("You walk down the pathway")
    time.sleep(2)
    print("It is getting brighter and brighter")
    time.sleep(2)
    print("You begin to see the end of the path, and...")
    print()
    time.sleep(2)

    friendlyPath = random.randint (right, left)

    if chosenPath== str(friendlyPath):
        print ("You got out!")
    else:
        print ("You found a dead end")

def chooseFood():
    global food
    food=' '
    while food != 'pancake' and food != 'waffle'
    print ('Which one do you want to eat? Pancakes or waffles?')
    food = input()

def checkFood(chosenFood):
    global food
    print("You found a tree")
    time.sleep(2)
    print("It is extremely tall")
    time.sleep(2)
    print("You begin to kick the tree, the tree shakes and...")
    print()
    time.sleep(2)

    friendlyFood = random.randint (pancake, waffle)

    if chosenFood== str(friendlyFood):
        print ("You got food!")
    else:
        print ("You're ded cuhhhhhhhhh")
        
def checkCastle (chosenCastle):
    global castle
    print('It is dark and fluffy')
    time.sleep (2)
    print ('It smells sweet and mellow')
    time.sleep(2)
    print (' a cake snake appears')
    time.sleep (4)

    friendlyCastle = random.randint(1, 2)

    if chosenCastle== str(friendlyCastle):
        print ('The snake slithered away')
    else:
        print ('The snake has bit you with its poisonous fangs')

def checkMountain (chosenMountain):
    global mountain
    print (' It is cold and moist')
    time.sleep(2)
    print('The mountains appears to be very tall. You begin to climb the mountain')
    time.sleep(2)
    print('A wild walmart employee comes around the aisle')
    time.sleep(4)

    friendlyMountain = random.randint(1,2)

    if chosenMountain == str(friendlyMountain):
        print('The employee scans the tags quietly')
    else:
        print('The emplyee kicks you off the mountain for attempted theft')
    

playAgain = 'yes'
while playAgain == 'yes' or playAgain =='y' :
    if 
        displayIntro()
        againNumber = chooseAgain()
        checkAgain(againNumber)
        if areaNumber = "1"
        

    print("Do you want to play again? (yes or no) ")
    playAgain = input()
