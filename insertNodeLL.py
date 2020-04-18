from room import Room
from player import Player
from item import Item
import argparse
import re

# Declare all the rooms
# https://www.futurelearn.com/courses/object-oriented-principles/0/steps/31490
# ADDING ITEM VERSUS LIST OF ITEMS TO LIST https://www.geeksforgeeks.org/append-extend-python/
itemnames = [
    Item("hammer"),
    Item("sheild"),
    Item("bucket"),
    Item("food"),
    Item("water"),
    Item("sword"),
    Item("blanket"),
    Item("shovel")

]


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [itemnames[0]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",  [itemnames[1]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",  [itemnames[2]]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",  [itemnames[3]]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",  [itemnames[4]]),
}


room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# set player attributes here
player = Player(input("Enter your player name: "),
                room['outside'], [itemnames[2]])

# print(player.current_room.Item.name[0][0])


def check():
    # rlist = [i for sub in player.current_room.Item[1] for i in sub]
    rlist = [Item("hammer"), Item("gloves")]
    rlist.append(player.current_room.Item)
    thing4 = player.getitem(player, rlist)
    # print("rlist", rlist)
    minput = ["take", "sheild"]
    print("playeritems: ", player.Item, minput[1])
    roomItems = []
    for i in player.current_room.Item[0]:
        roomItems.append(i)
    for i in roomItems:
        print(type(i))

    print("here", roomItems[0])

    # print("thing4", thing4)


"""
get = input(
    "choose an item by typing [take] [itemname] or choose [q]: ")
# \s stands for white chars and + for reps of \s char
ans = get.split()

print(ans)
"""

"""
def check():
    get = input(
        "choose an item by typing [take] [itemname] or choose [q]: ")
    # if get in player.current_room.Item.name[0][0] and "take" in get:
    ran = get.split()
    if "take" in ran:
        print("yep")
    if get == "q":
        print("no items chosen from room")
    elif ran[1] in player.current_room.Item.name[0][0]:
        player.getitem(player, ran[1], ran[2])
        thing1 = [i for i in player.Item.name[0]]
        thing1.remove(ran[1])
        thing2 = []
        thing2.append(thing1[1])
        # print("here", thing2)
"""


def getDirection():  # decouple function to take care of getting direction input
    mydir = ["n", "s", "w", "e"]
    print("hint: ")
    for i in mydir:
        newroom = player.current_room.roomDirection(i)
        if newroom:
            print(f"\n{i} will move to {newroom}")
    direction = input("which direction? [n/s/w/e]: ")
    if direction == "n" or direction == "s" or direction == "w" or direction == "e":
        return direction
    else:
        print("Invalid direction")
        return getDirection()  # regression


def moveRoom(player, direction):
    # direction passed here is result of getDirection() function input
    newRoom = player.current_room.roomDirection(direction)
    if newRoom:
        player.move1(newRoom)
    else:
        print("Oops can't go in that direction, retry!")
        newDirection = getDirection()
        moveRoom(player, newDirection)  # regression


def takeItem(player, room):
    if len(player.current_room.Item) == 0:
        print("no items in room to pick up")
    else:
        get = input(
            "choose an item by typing [take] [itemname] or choose [no] [item]: ")
        spltInput = get.split()
        if "no" in spltInput:
            print("no items chosen from room")
        elif "take" in spltInput:
            print("take chosen. splInput[1] is", spltInput[1])
            for x in range(len(player.current_room.Item)):
                if spltInput[1] == str(player.current_room.Item[x]):
                    print(
                        f"\n you have picked up {player.current_room.Item[x]}")
                    # doesn't use the getitem method
                    player.Item.append(player.current_room.Item[x])
                    del player.current_room.Item[x]
                    break


def dropItem(player, room):
    get = input(
        "Drop an item by typing [drop] [itemname] or choose [dont] [drop]: ")
    spltInput = get.split()
    # print("YO", player.Item.name[0])
    if "dont" in spltInput:
        print("no items dropped")
        print("TEST", len(player.Item))
        for x in range(len(player.Item)):
            print(player.Item[x])
        return
    if "drop" in spltInput:
        if len(player.Item) > 0:
            for x in range((len(player.Item)+1)):
                if spltInput[1] == str(player.Item[x]):
                    print(f"\n you have dropped {player.Item[x]}")
                    player.current_room.Item.append(player.Item[x])
                    player.Item.pop(x)
                    break
    if len(player.current_room.Item) > 0:
        print(f"\n {player.current_room} now has: ")
        for x in range(len(player.current_room.Item)):
            print(f"\n {player.current_room.Item[x]}")
    else:
        print("try again")


def inventory(player):
    inv = input(
        "To check items carried by player type [i] or [inventory] else type [continue] or [q] to quit: ")
    spltInv = inv.split()
    if "i" in spltInv or "inventory" in spltInv:
        print(f"\n {player.name} currently carrying: \n")
        if len(player.Item) > 0:
            for x in range(len(player.Item)):
                print(f"\n{player.Item[x]}")
        return
    if "continue" in spltInv:
        print("game continue")
        return
    if "q" in spltInv:
        print("\n You've Quit Game")
        exit()
    else:
        print("invalid command")
        inventory(player)


def loopGame():
    global player
    if len(player.current_room.Item) > 0:
        for x in range(len(player.current_room.Item)):
            print(
                f'\n {player.name} is in the {player.current_room}, this room contains {player.current_room.Item[x]} ')
    else:
        print(
            f'\n{player.name} is in the {player.current_room}. This room currently has no items to pick up')
    direction = getDirection()
    moveRoom(player, direction)
    for x in range(len(player.current_room.Item)):
        print(
            f'\n {player.name} entered the {player.current_room}, this room contains {player.current_room.Item[x]} ')
    takeItem(player, room)
    dropItem(player, room)
    inventory(player)
   # check()


def main():
    while True:
        loopGame()


main()
