# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.




def main():
    rooms = {
        'School Entrance': {'north': 'Hallway', 'east': 'Auditorium'},
        'Hallway': {'north': 'Annex', 'south': 'School Entrance', 'east': 'Science Class', 'west': 'English Class'},
        'Annex': {'north': 'Gym', 'south': 'Hallway', 'east': 'Lunch Room', 'west': 'Math Class'},
        'Gym': {'north': 'Locker Room', 'south': 'Annex', 'Staff': 'Janitor'},  # janitor starting position
        'Locker Room': {'south': 'Gym', 'Item': 'Gym Clothes'},
        'Auditorium': {'west': 'School Entrance', 'Item': 'Book Bag', 'Staff': 'Janitor'}, # janitor position after 6 moves
        'English Class': {'east': 'Hallway', 'Item': 'English Book'},
        'Math Class': {'east': 'Annex', 'Item': 'Math Book', 'Staff': 'Math Teacher'},
        'Science Class': {'west': 'Hallway', 'Item': 'Science Book'},
        'Lunch Room': {'west': 'Annex', 'Item': 'Jacket', 'Staff': 'Janitor'},  # janitor position after 3 moves
    }

    # tracks items gathered by user
    inventory = []

    # moves counter
    moves = 0

    # caught detection
    caught = 0
    alarmON = 0

    # win detection
    win = 'No'

    # janitor status
    janitorHome = 'No'

    clear()
    intro()

    # start gameplay loop
    while True:
        if caught == 1 or win == 'Yes':
            break
        clear()
        enterExit = start_quit()
        clear()

        # enter school conditional
        if enterExit == 'enter':
            currentRoom = 'School Entrance'
            print(f'You have entered the school without being detected!\n')
            pause()

            # move through school loop
            while True:
                clear()
                print(f'Current room: {currentRoom}')
                direction = get_nsew()
                clear()

                if direction == 'exit':
                    break

                nextRoom = move_rooms(currentRoom, direction, rooms)
                if nextRoom != currentRoom:
                    moves += 1
                    currentRoom = nextRoom
                    print(f'You moved {direction}, Current room: {currentRoom}')

                else:
                    print(f'Can\'t move {direction} from {currentRoom}.\n')
                    pause()

                # Math Teacher encounter
                if 'Staff' in rooms[currentRoom].keys() and currentRoom == 'Math Class' and moves < 5:
                    caught += 1
                    clear()
                    print(
                        f'{rooms[currentRoom]['Staff']} has spotted you at school after hours and has kicked you out.')
                    print(f'All doors are now locked and you can no longer get back in.\n\n')
                    pause()
                    break

                # Math Teacher Goes Home
                if moves == 5:
                    clear()
                    print('Math Teacher has gone home for the day. It is safe to grab your Math Book.\n\n')
                    pause()
                    clear()

                # Janitor encounter
                if 'Staff' in rooms[currentRoom].keys():
                    if moves > 6:
                        if 'Staff' in rooms[currentRoom].keys() and currentRoom == 'Auditorium':
                            caught += 1
                            clear()
                            print(
                                f'{rooms[currentRoom]['Staff']} has spotted you at school after hours and has kicked you out.')
                            print(f'All doors are now locked and you can no longer get back in.\n\n')
                            pause()
                            break

                    elif 3 < moves < 7:
                        if 'Staff' in rooms[currentRoom].keys() and currentRoom == 'Lunch Room':
                            caught += 1
                            clear()
                            print(
                                f'{rooms[currentRoom]['Staff']} has spotted you at school after hours and has kicked you out.')
                            print(f'All doors are now locked and you can no longer get back in.\n\n')
                            pause()
                            break

                    else:
                        if 'Staff' in rooms[currentRoom].keys() and currentRoom == 'Gym':
                            caught += 1
                            clear()
                            print(
                                f'{rooms[currentRoom]['Staff']} has spotted you at school after hours and has kicked you out.')
                            print(f'All doors are now locked and you can no longer get back in.\n\n')
                            pause()
                            break

                # Janitor Goes Home
                if moves >= 10 and len(inventory) == 5 and janitorHome == 'No':
                    alarmON = moves + 5
                    janitorHome = 'Yes'
                    clear()
                    print(
                        'Janitor has gone home for the day and preped the alarm system. You only have 5 more moves till the alarm system detects you.\n\n')
                    pause()
                    clear()

                # item indicator and add item to inventory
                if 'Item' in rooms[currentRoom].keys():
                    item = rooms[currentRoom]['Item']
                    if item not in inventory:
                        print(f'You see your {item}.\n')
                        input(f'Press enter to grap your {item}...')
                        inventory.append(rooms[currentRoom]['Item'])
                        clear()
                        print(f'{item} retrieved\n')
                        pause()

                # alarm system detection
                if moves == alarmON:
                    caught += 1
                    clear()
                    print(
                        f'You took too long to find all of your items and got caught by the alarm system. You have been expelled!\n')
                    pause()
                    break

                # winning game condition
                if len(inventory) == 6:
                    win = 'Yes'
                    clear()
                    print(f'Congratulations! You have found all of your books and have passed all of your exams!\n')
                    pause()
                    break

        elif enterExit == 'quit':
            break


# define function to get north, south, east, and west. Also exit school command
def get_nsew():
    while True:
        try:
            NSEW = input('Direction: ').lower()
            if NSEW == 'north' or NSEW == 'south' or NSEW == 'east' or NSEW == 'west' or NSEW == 'exit':
                return NSEW
            else:
                print('Not a valid entry. Choose "north", "south", "east", or "west". Type "exit" to leave the school.')
        except ValueError:
            print('Not a valid entry. Choose "north", "south", "east", or "west". Type "exit" to leave the school.')


# define function to start and quit the game
def start_quit():
    while True:
        try:
            SE = input('''START MENU: Type "enter" to enter the school or "quit" to quit game.
>''').lower()
            if SE == 'enter' or SE == 'quit':
                return SE
            else:
                clear()
                print('Not a valid entry.')
        except ValueError:
            clear()
            print('Not a valid entry.')


# define function to move through rooms
def move_rooms(current_room, direction, rooms):
    if direction in rooms[current_room] and rooms[current_room][direction]:
        return rooms[current_room][direction]
    else:
        return current_room


# define function to pause the game until user hits enter
def pause():
    input('Press Enter to continue...')


# define function that displays start menu and game instructions
def intro():
    print('\t\t---Welcome to Green Valley High School---\n\n\
        You are a student at Green Valley High Shcool and have forgotten several items back at school.\n\
        You must collect all of your items without getting caught in order to pass your tests tomorrow.\n\n\
        Directions:\t"north, south, east, or west" allows you to move from room to room\n\
        \t\t\tPressing the "Enter" key (adds items to your inventory)\n\n')

    pause()


# define function that clears the terminal
def clear():
    import os

    os.system('cls' if os.name == 'nt' else 'clear')






if __name__ == '__main__':
    main()



