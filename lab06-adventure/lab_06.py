class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
def main():
    room_list = []
    current_room = 0
    next_room = 0
    done = False
    room = Room("Sala de inicio. n, s.", 1, 7, 2, None)
    room_list.append(room)
    room = Room("Sala 1. n, s, w", 5, None, 0, 3)
    room_list.append(room)
    room = Room("Sala 2. n, w", 0, None, None, 4)
    room_list.append(room)
    room = Room("Sala 3. e", None, 1, None, None)
    room_list.append(room)
    room = Room("Sala 4. e", None, 2, None, None)
    room_list.append(room)
    room = Room("Sala 5. s, w", None, None, 6, 1)
    room_list.append(room)
    room = Room("Sala 6. n, e", 5, 9, None, None)
    room_list.append(room)
    room = Room("Sala 7. e, s, w", None, 9, 8, 0)
    room_list.append(room)
    room = Room("Sala 8. n", 7, None, None, None)
    room_list.append(room)
    room = Room("Sala 9. s w", None, None, 7, 6)
    room_list.append(room)
    print(room_list[current_room].description)
    while not done:
        print()
        print(room_list[current_room].description)
        voy = input('¿Ande vas?\n')
        if voy == None:
            print('¡¡Pa allá no, brouston!!')
            next_room = current_room
        elif voy.lower() == 'n' or voy.lower() == 'north':
            next_room = room_list[current_room].north
        elif voy.lower() == 'e' or voy.lower() == 'east':
            next_room = room_list[current_room].east
        elif voy.lower() == 's' or voy.lower() == 'south':
            next_room = room_list[current_room].south
        elif voy.lower() == 'w' or voy.lower() == 'west':
            next_room = room_list[current_room].west
        elif voy.lower() == 'quit':
            done = True
        else:
            print('¡¡Pa allá no, brouston!!')
            next_room = current_room
        if next_room == None:
            print('Te estampas contra una pared.')
            next_room = current_room
        else:
            current_room = next_room


main()