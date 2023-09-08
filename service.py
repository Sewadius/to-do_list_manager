# Constants and some functions
from pathlib import Path

# Integer constants for choosing options in main menu
MIN_CHOICE, MAX_CHOICE = 1, 7

# String constants for task status and messages
WRONG_TASK = 'You entered the wrong task number! Try again'
EMPTY_LIST = 'To-Do List: (Empty)'
UNFULFILLED = 'unfulfilled'
FULFILLED = 'fulfilled'

# Path and file name constants
PATH = Path('./json/todo.json')  # Path fo .json file
FILE_NAME = 'json/todo.json'  # File name


def print_greeting() -> None:
    """Prints the greeting from the programme"""
    print('''=== To-Do List Manager ===
1. Display To-Do List
2. Add Task
3. Mark task as fulfilled
4. Remove task via number
5. Remove all fulfilled tasks
6. Clear all tasks
7. Quit
''')


def print_menu_hint() -> None:
    print('Also you may type "menu" anytime to show this info again\n')


def clear_file() -> None:
    """Initially clears the .json file"""
    open(FILE_NAME, 'w').close()


def print_dict(tasks: dict) -> None:
    """Prints all current items"""
    print('\nTo-Do List:')
    i = 1
    while tasks.get(str(i)):
        task, status = tasks[str(i)][0], tasks[str(i)][1]
        print(f'{i}. {task} ({status})')
        i += 1
    print()
