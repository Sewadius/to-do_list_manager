#!/usr/bin/python3
import os
from pathlib import Path

MIN_CHOICE, MAX_CHOICE = 1, 4

PATH = Path('./todo.txt')       # Path fo .txt file
FILE_NAME = 'todo.txt'          # File name
list_to_do = []                 # List to do for handling file


def print_greeting() -> None:
    """Prints the greeting from the programme"""
    print('''=== To-Do List Manager ===
1. Display To-Do List
2. Add Task
3. Remove Task
4. Quit
''')


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


def handle_user_choice(select: int) -> bool:
    """Process the correct user's choice"""
    match select:
        case 1:     # Display To-Do list
            display_to_do_list()
        case 2:     # Add task to file
            add_task_to_list()
        case 3:     # Remove task
            remove_task_from_list()
        case 4:     # Quit
            print('Goodbye!')
            return False
    return True


def display_to_do_list() -> None:
    """Reading form file and show all entries"""
    if not PATH.is_file():                  # Check file is exist
        print('There are no entries in the file!')
        return
    if os.stat(FILE_NAME).st_size == 0:     # Check file is empty
        print('\nTo-Do List: (Empty)')
        return
    print('\nTo-Do List:')
    i = 1
    with open(FILE_NAME, 'r') as file:
        for line in file:
            print(f'{i}. {line}', end='')
            i += 1
    print()


def add_task_to_list() -> None:
    """Add a new task to file 'todo.txt'"""
    task = input('Enter the task to add: ')
    if task not in list_to_do:
        with open(FILE_NAME, 'a') as file:
            file.write(f'{task}\n')
        list_to_do.append(task)
    else:
        print('This entry is already in list!')


def remove_task_from_list() -> None:
    """Remove the existing task from file"""
    if not list_to_do:
        print('You have no items in to-do list!')
        return
    try:
        task = int(input('Enter the task number to remove: '))
        if 0 < task <= len(list_to_do):
            element_for_delete = list_to_do[task - 1]
            del list_to_do[task - 1]
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
    while select_user_choice():
        pass
