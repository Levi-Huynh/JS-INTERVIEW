from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()

"""
input: graph with 500 nodes/verts
output: trav path - with directions, when walked in order, vists _every_ room at least once (BFT?)


# Start by writing an algorithm that picks a random unexplored direction from the player's current room
visited ={} dict
setDir = {} dict
# def: explore & log Room (self)    #(PUTS RANDOM DIRECTION IN player.travel, RETURN NEW ROOM)

    for dir in player.current_room.get_exits():
        if dir is not None:
            room_id= player.travel(dir)
            setDir[dir] = '?' # setDir[dir] = "?"
            visted[room_id] = setDir



"""


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    # basically a path that visits each room, easy
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
"""

player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")

"""

setDir = {}


def travel(path):  # this explores & logs all room's direction & their corresp room to visited_rooms
    stor = []
    for i in path:  # [n,s,w]
        roomID = player.travel(i)
        stor.append(roomID)


def explore1(player)
 print("curr", player.current_room.id)
  myL = []
   for dir in player.current_room.get_exits():
        mL.append(dir)

    return mL  # [ n, s , w,e ]


def dft(start_room, visited):
    q = Queue()
    q.enqueue([start_room])
    # visited = set()

    while q.size() > 0:
        # path = room_id =0
        path = q.dequeue() 
        room = path[-1]

        if room not in visited:
            for ele in path:
                setDir[ele] : "?"
                visited_room[room] = setDir 
        if visited_room[room] == "?":
                roomList= travel(path)
                # room id => #direction 
                # room id list needs to be appended to be added to visit_rooms
                # add to visited rooms 
                # [n,s, w, e]
                dirList = explore1()
                newPath = [*path]
                newPath.append(e)
                q.enqueue(newPath)


# trav_path = ['n','n' conversion of room_id]

# visited_room = {roomId {'n':'?', 's': n, 'w':'?', 'e': '?'}
# }
