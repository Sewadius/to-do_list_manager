#!/usr/bin/python3
import os
import json
from service import *

counter = 1         # Counter for items in list
dict_to_do = {}     # Dictionary to do for handling file


def clear_to_do_dict() -> None:
    """Clears items from the dictionary"""
    global counter
    counter = 1
    dict_to_do.clear()
    print('All items were deleted!')


def clear_all() -> None:
    """Clears json file and the dictionary"""
    clear_file()
    clear_to_do_dict()


def write_dict_to_json_file() -> None:
    """Writes local dictionary to json file"""
    json_object = json.dumps(dict_to_do)
    with open(FILE_NAME, 'w') as file:
        file.write(json_object)


def select_user_choice() -> bool:
    """Get the choice from user"""
    try:
        value = input('Enter your choice: ')
        if value.lower() == 'menu':
            print_greeting()
            return True
        value = int(value)
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
        case 1:  # Display To-Do list
            display_to_do_list()
        case 2:  # Add task to file
            add_task_to_list()
        case 3:  # Mark task as fulfilled
            mark_as_fulfilled()
        case 4:  # Remove task via number
            remove_task_from_list()
        case 5:  # Remove all fulfilled tasks
            remove_fulfilled_tasks()
        case 6:  # Clear all tasks
            clear_all()
        case 7:  # Quit
            print('Goodbye!')
            return False
    return True


def display_to_do_list() -> None:
    """Reading form json file and show all entries"""
    if os.stat(FILE_NAME).st_size == 0:     # Check file is empty
        print(EMPTY_LIST)
        return

    with open(FILE_NAME, 'r') as file:
        json_object = json.load(file)
        if not json_object:
            print(EMPTY_LIST)
            return

    print_dict(json_object)


def add_task_to_list() -> None:
    """Add a new task to file 'todo.json'"""
    global counter
    task = input('Enter the task to add: ')
    for el in dict_to_do.values():
        if el[0] == task:
            print('This entry is already in list!')
            return
    dict_to_do[counter] = [task, UNFULFILLED]
    write_dict_to_json_file()
    counter += 1


def mark_as_fulfilled() -> None:
    """Mark a task as fulfilled in list"""
    try:
        task = int(input('Enter the task number to mark as fulfilled: '))
        if 0 < task <= len(dict_to_do):
            element = dict_to_do.get(task)
            element[1] = FULFILLED
            dict_to_do[task] = element
            write_dict_to_json_file()
            print(f'Task "{element[0]}" marked as fulfilled!')
        else:
            print(WRONG_TASK)
            mark_as_fulfilled()
    except ValueError:
        print(WRONG_TASK)
        mark_as_fulfilled()


def remove_task_from_list() -> None:
    """Remove the existing task from file"""
    global counter
    try:
        task = int(input('Enter the task number to remove: '))
        if 0 < task <= len(dict_to_do):
            element_for_delete = dict_to_do.get(task)
            dict_to_do.pop(task)
            counter -= 1
            write_dict_to_json_file()
            print(f'Task "{element_for_delete[0]}" was successfully deleted!')
        else:
            print(WRONG_TASK)
            remove_task_from_list()
    except ValueError:
        print(WRONG_TASK)
        remove_task_from_list()


def remove_fulfilled_tasks() -> None:
    """Removes all fulfilled tasks from the dictionary"""
    global counter, dict_to_do
    items_for_remove = [
        el for el in dict_to_do.values() if el[1] == FULFILLED
    ]
    counter -= len(items_for_remove)
    dict_to_do = {k: v for k, v in dict_to_do.items() if v not in items_for_remove}
    write_dict_to_json_file()
    print('All fulfilled tasks has been removed!')


if __name__ == '__main__':
    print_greeting()
    print_menu_hint()
    clear_file()
    while select_user_choice():
        pass
