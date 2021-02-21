#! /usr/bin/env python3

from enum import Enum
from typing import List, Dict, Any


class cmds(str, Enum):
    Yes = 'y'
    No = 'n'


# Check strings.
yn = 'y/n :'
redcheck = "Any Red wires?"
lastwhite = "Last wire white?"
multiblues = 'More than 1 blue wire?'
serialodd = 'Is the last digit of the serial number odd?'


# Cutting Strings.
cut_1st = "Cut 1st wire."
cut_2nd = "Cut 2nd wire."
cut_3rd = "Cut 3rd wire."
cut_4th = "Cut 4th wire."
cut_last = "Cut last Wire."
cut_last_col = 'Cut the last {} wire.'


def three(order):
    if 'r' not in order:
        print(cut_2nd)
    elif order[-1] == 'w':
        print(cut_last)
    elif order.count('b') > 1:
        print(cut_last_col.format('BLUE'))
    else:
        print(cut_last)
    return


def four(order):
    if order.count('r') > 1:
        resp = input(serialodd + yn)
        if resp == cmds.Yes:
            print(cut_last_col.format('RED'))
            return

    if order[-1] == 'y':
        if 'r' not in order:
            print(cut_1st)
    elif order.count('b') == 1:
        print(cut_1st)
    elif order.count('y') > 1:
        print(cut_last)
    else:
        print(cut_2nd)
    return


def five(order):
    if order[-1] == 'k':
        resp = input(serialodd + yn)
        if resp == cmds.Yes:
            print(cut_4th)
            return
    if order.count('r') == 1 and order.count('y') > 1:
        print(cut_1st)
    elif 'k' not in order:
        print(cut_2nd)
    else:
        print(cut_1st)


def six(order):
    if order.count('y') == 0:
        resp = input(serialodd + yn)
        if resp == cmds.Yes:
            print(cut_3rd)
            return
    if order.count('y') == 1 and order.count('w') > 1:
        print(cut_4th)
    elif order.count('r') == 0:
        print(cut_last)
    else:
        print(cut_4th)


conv_d = {
    'r': 'red',
    'k': 'black',
    'y': 'yellow',
    'b': 'blue',
    'w': 'white',
    'x': 'otherwise'
}

curr_cmd = cmds.Yes
print("Wire conversion table:\n     Color | Input")
for i, j in conv_d.items():
    print(j.rjust(10), '|', i)
order = input("What's the order top-to-bottom?\n")
wire_count = len(order)
while not all([i in conv_d for i in order]) or (wire_count not in range(3, 7)):
    print("\033[FThat's not a valid sequence.")
    order = input("What's the order top-to-bottom?\n")
    wire_count = len(order)

print('\033[F', end='')
if wire_count == 3:
    three(order)
elif wire_count == 4:
    four(order)
elif wire_count == 5:
    five(order)
else:
    six(order)
