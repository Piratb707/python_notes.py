# Python Text RPG
# Name here :D

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100


##### Player Setup #####
class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'start'
        self.game_over = False
myPlayer = player()


#####  Titlle Screen #####
def title_screen_selection():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['paly', 'help', 'quit']:
        print("Please enter a valid command")
        option = input("> ")
        if option.lower() == ("play"):
            start_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()


def title_screen():
    os.system('clear')
    print("###########################")
    print("# Welcome to the Text RPG #")
    print("###########################")
    print("           Play            ")
    print("           Help            ")
    print("           Quit            ")
    print("  Copyright 2023 SpaVodka  ")
    title_screen_selection()


def help_menu():
    os.system('clear')
    print("###############################")
    print("### Welcome to the Text RPG ###")
    print("###############################")
    print("Euse Up,Down,Left,Right to move")
    print("Type your commands to do them  ")
    print("Use 'Look' to inspect something")
    print("    Copyright 2023 SpaVodka    ")
    title_screen_selection()


##### MAP ######
"""
a1 a2.. # {layer Starts at b2 
---------
| | | | | a4
---------
| | | | | b4
---------
| | | | |
---------
| | | | |
---------
"""
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False
                 }
zonemap = {
    'a1': {
        ZONENAME: "Town Market",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2',
    },
    'a2': {
        ZONENAME: "Town Entrace",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3',
    },
    'a3': {
        ZONENAME: "Town Square",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4',
    },
    'a4': {
        ZONENAME: "Town Hall",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: '',
    },
    'b1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a1',
        DOWN: 'c1',
        LEFT: '',
        RIGHT: 'b2',
    },
    'b2': {
        ZONENAME: "Home",
        DESCRIPTION: 'This is your home',
        EXAMINATION: 'Your home looks the same',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    'b3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'b4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'c1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'c2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'c3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'c4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'd1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'd2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'd3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'd4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    }
}


##### GAME INTERACTIVITY #####
def print_location():
    print('\n' + ("#" * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location.upper() + ' #')
    print('# ' + zonemap[myPlayer.positiom][DESCRIPTION] + ' #')
    print('\n' + ("#" * (4 + len(myPlayer.location))))


def promt():
    print("\n" + "========================")
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_action:
        print("Unknown action, try again.\n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())


def player_move(myAction):
    ask = "Where would you like to move?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)


def movement_handler(destination):
    print("\n" + "You have move to the " + destination + ".")
    myPlayer.location = destination
    print_location()


def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("You have already exhausted this zone")
    else:
        print("You can trigger a puzzle here.")


##### GAME FUNCTIONALITY #####
def start_game():
    return


def main_game_loop():
    while myPlayer.game_over is False:
        prompt()


def setup_game():
    os.system('clear')

    ### NAME COLLECTING ###
    question1 = "Hello, what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    ### JOB HANDLING ###
    question2 = "What the role you want to play?\n"
    question2_class_selection = "(You can play as a warrior, priest, mage)\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2_class_selection:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input("> ")
    valid_jobs = ['Warrior', 'mage', 'priest']
    if palyer_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("You are now a " + player_job + "!\n")
    while player_job.lower() not in valid_jobs:
        player_job = input("> ")
        if palyer_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("You are now a " + player_job + "!\n")

    if myPlayer.job == "warrior":
        self.hp = 120
        self.mp = 20
    elif myPlayer.job == "mage":
        self.hp = 40
        self.mp = 100
    elif myPlayer.job == "priest":
        self.hp = 80
        self.mp = 60

    ### INTRODUCTION ###
    question3 = "Welcome, " + player_name + " the " + player_job + ".\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    speech1 = "Welcome to this fantasy world!"
    speech2 = "I hope it greets you well!"
    speech3 = "Just make sure you don't get too lost..."
    speech4 = "Hehehehe..."
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)

    os.system('clear')
    print("######################")
    print("#  Let's start now!  #")
    print("######################")
    main_game_loop()


title_screen()
































