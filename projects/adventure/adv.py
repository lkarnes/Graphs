from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
import sys

sys.setrecursionlimit(2000)
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
graph = {}

def get_opposite(dir):
    if dir == 'n':
        return 's'
    if dir == 's':
        return 'n'
    if dir == 'e':
        return 'w'
    if dir == 'w':
        return 'e'

def dft(path = []):
    current_room = player.current_room
    if current_room.id not in graph:
        graph[current_room.id] = {}
    exits = current_room.get_exits()
    unvisited = []
    for d in exits:
        if d not in graph[current_room.id]:
            graph[current_room.id][d] = '?'
            unvisited.append(d)
        else:
            if graph[current_room.id][d] == '?':
                unvisited.append(d)
    if any('?' in g.values() for g in graph.values()):
        if len(unvisited) > 1:
            rand = random.randint(0,len(unvisited)-1)
            rand_direction = unvisited[rand]
            path.append(rand_direction)
            player.travel(rand_direction)
            traversal_path.append(rand_direction)
            graph[current_room.id][rand_direction] = player.current_room.id
            if player.current_room.id not in graph:
                graph[player.current_room.id] = {}
            graph[player.current_room.id][get_opposite(rand_direction)] = current_room.id
        elif len(unvisited) == 0:
                if len(path) != 0: 
                    move = get_opposite(path.pop())
                    traversal_path.append(move)
                    player.travel(move)
                else:
                    traversal_path.append(current_room)
                    return None
        else:
            path.append(unvisited[0])
            player.travel(unvisited[0])
            graph[current_room.id][unvisited[0]] = player.current_room.id
            traversal_path.append(unvisited[0])
            if player.current_room.id not in graph:
                graph[player.current_room.id] = {}
            graph[player.current_room.id][get_opposite(unvisited[0])] = current_room.id
        dft(path)
        
# def dft():
#     s = []
#     s.append(player.current_room)
#     while len(s) > 0:
#         location = s.pop()
#         directions = location.get_exits()
#         path = []
#         new_dir = []
#         for d in directions:
#             if location.id not in graph:
#                 graph[location.id] = {}
#             if d not in graph[location.id]:
#                 graph[location.id][d] = '?'
#                 new_dir.append(d)
#         directions = new_dir     
                
#         print(location.id, [(d, graph[location.id][d]) for d in directions])
#         if len(directions) > 1:
#             rand = random.randint(0,len(directions)-1)
#             rand_direction = directions[rand]
            
#             while graph[location.id][rand_direction] != '?' and len(directions) > 1:
#                 directions.pop(rand)
#                 rand = random.randint(0,len(directions)-1)
                
#             player.travel(rand_direction)
#             s.append(player.current_room)
#             graph[location.id][rand_direction] = player.current_room.id
            
#             if player.current_room.id not in graph:
#                 graph[player.current_room.id] = {}
                
#             graph[player.current_room.id][get_opposite(rand_direction)] = location.id
#             path.append(rand_direction)
            
#         if len(directions) == 1 and graph[location.id][directions[0]] == '?':
#             player.travel(directions[0])
#             path.append(directions[0])
#             graph[location.id][directions[0]] = player.current_room.id
#             if player.current_room.id not in graph:
#                 graph[player.current_room.id] = {}
#             graph[player.current_room.id][get_opposite(directions[0])] = location.id
#             s.append(player.current_room)
        
#         if len(directions) == 0:
#             while len(path) > 0:
#                 back = path.pop()
#                 if back == 'n':
#                     player.travel('s')
#                 if back == 's':
#                     player.travel('n')
#                 if back == 'e':
#                     player.travel('w')
#                 if back == 'w':
#                     player.travel('e')
dft()
print(graph)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
