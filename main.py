#!/usr/bin/python3
import os
from pathlib import Path

# Integer constants for choosing options in main menu
MIN_CHOICE, MAX_CHOICE = 1, 5

# String constants for task status
UNFULFILLED = "unfulfilled"
FULFILLED = "fulfilled"

counter = 1                           # Counter for items in list

PATH = Path('./json/todo.json')       # Path fo .json file
FILE_NAME = 'json/todo.json'          # File name
dict_to_do = {}                       # Dictionary to do for handling file


def print_greeting() -> None:
    """Prints the greeting from the programme"""
    print('''=== To-Do List Manager ===
1. Display To-Do List
2. Add Task
3. Remove Task
4. Clear all tasks
5. Quit
''')


def clear_file() -> None:
    """Initially clears the .json file"""
    open(FILE_NAME, 'w').close()


def clear_to_do_list() -> None:
    dict_to_do.clear()
    print('All items were deleted!')


def select_user_choice() -> bool:
    """Get the choice from user"""
    try:
        value = int(input('Enter your choice: '))
        if value < MIN_CHOICE or value > MAX_CHOICE:
            print('You entered incorrect choice! Try again')
            select_user_choice()
        return handle_user_choice(value)
    except ValueError:
        print('You entered not a number! Try again')
        select_user_choice()
        return True


def handle_user_choice(select: int) -> bool:
    """Process the correct user's choice"""
    match select:
        case 1:     # Display To-Do list
            display_to_do_list()
        case 2:     # Add task to file
            add_task_to_list()
        case 3:     # Remove task
            remove_task_from_list()
        case 4:     # Clear all tasks
            clear_file()
            clear_to_do_list()
        case 5:     # Quit
            print('Goodbye!')
            return False
    return True


def display_to_do_list() -> None:
    """Reading form file and show all entries"""
    if not PATH.is_file():                  # Check file is exist
        print('There are no entries in the file!')
        return
    if os.stat(FILE_NAME).st_size == 0:     # Check file is empty
        print('To-Do List: (Empty)')
        return
    print('\nTo-Do List:')
    i = 1
    with open(FILE_NAME, 'r') as file:
        for line in file:
            print(f'{i}. {line}', end='')
            i += 1
    print()


def add_task_to_list() -> None:
    """Add a new task to file 'todo.json'"""
    task = input('Enter the task to add: ')
    if task not in dict_to_do.values():
        print('Yes')
        # with open(FILE_NAME, 'a') as file:
        #     file.write(f'{task}\n')
        dict_to_do[counter] = [task, UNFULFILLED]
    else:
        print('This entry is already in list!')


def remove_task_from_list() -> None:
    """Remove the existing task from file"""
    try:
        task = int(input('Enter the task number to remove: '))
        if 0 < task <= len(dict_to_do):
            element_for_delete = dict_to_do[task - 1]
            del dict_to_do[task - 1]
            # Remove from file
            with open(FILE_NAME, 'r') as file:
                lines = file.readlines()
            with open(FILE_NAME, 'w') as file:
                for line in lines:
                    if line.strip('\n') != element_for_delete:
                        file.write(line)
            print(f'Entry "{element_for_delete}" was successfully deleted!')
        else:
            print('There is no this task number! Try again')
            remove_task_from_list()
    except ValueError:
        print('You entered the wrong task number! Try again')


if __name__ == '__main__':
    print_greeting()
    clear_file()
    while select_user_choice():
        pass
