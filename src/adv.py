from room import Room
from player import Player
from items import Items
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Declare Items

item = {
    'pen': Items('pen', 'Writes clearly and permanent, but is susceptible to heat.'),
    'pencil': Items('pencil', 'Made of wood and graphite, this weapon provides users with the ability to undo work.'),
    'keyboard': Items('keyboard', 'This implement is useless without a computer.'),
    'lipstick': Items('lipstick', 'Crude and a little ominous-looking when used for writing.'),
    'brush': Items('brush', 'Requires paint')
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#Items Placed in room:
room['outside'].items.append(item['keyboard'])

# Main
#

# Make a new player object that is currently in the 'outside' room.
player_room = room['outside']
player = Player(player_room)
# Write a loop that:
while True:
    location = player.location
#
# * Prints the current room name
    print(f'You are now in {location.name_room}')
# * Prints the current description (the textwrap module might be useful here).
    print(f'Looking around you see, {location.description_room} \n')
    print(f'this room contains, \n{location.items}\n')
# * Waits for user input and decides what to do.
#
    print("What's yr next move?")
    print('Enter n, s, e, or w')
    print('to quit type `q`\n')
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    command = input('>').split(',')

    if command[0] == 'n':
        if hasattr(location, 'n_to'):
            print("\nWalk North")
            player.location = location.n_to
        else:
            print('Not a valid more, try again \n')

    elif command[0] == 's':
        if hasattr(location, 's_to'):
            print('\nWalk south')
            player.location = location.s_to
        else:
            print('Not a valid more, try again \n')

    elif command[0] == 'w':
        if hasattr(location, 'w_to'):
            print('\nWalk west')
            player.location = location.w_to
        else:
            print('Not a valid more, try again \n')

    elif command[0] == 'e':
        if hasattr(location, 'e_to'):
            print('\nWalk east')
            player.location = location.e_to
        else:
            print('Not a valid more, try again \n')

    elif command[0] == 'q':
        print('yr a quitter \n')
        exit()
