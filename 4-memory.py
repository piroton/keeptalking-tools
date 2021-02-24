#! /usr/bin/env python3

import re


pa = "Press Button A."
pb = "Press Button B."
pc = "Press Button C."
pd = "Press Button D."
px = "Press Button {}."
p4 = "Press Button LABELED 4."
pl = "Press Button LABELED {}."


keya = """+---------------+
|    DISPLAY    |"""
keyb = """+---------------+
| A | B | C | D |
+---------------+
"""
print("This is the notation of the module.")
print(keya)
print(keyb)
print()

pos = []
labels = []
for stage in range(1, 6):
    print("What's on the DISPLAY?")
    display = input()
    print('\033[F', end='')
    while display not in ['1', '2', '3', '4']:
        print("That's not right.")
        print("What's on the DISPLAY?")
        display = input()
        print('\033[F', end='')

    int_disp = int(display)

    if stage == 1:
        if int_disp == 1 or int_disp == 2:
            print(pb)
        elif int_disp == 3:
            print(pc)
        else:
            print(pd)

    elif stage == 2:
        if int_disp == 1:
            print(p4)
        elif int_disp == 3:
            print(pa)
        else:
            print(px.format(pos[0]))

    elif stage == 3:
        if int_disp == 1:
            print(pl.format(labels[1]))
        elif int_disp == 2:
            print(pl.format(labels[0]))
        elif int_disp == 3:
            print(pc)
        else:
            print(p4)

    elif stage == 4:
        if int_disp == 1:
            print(px.format(pos[0]))
        elif int_disp == 2:
            print(pa)
        else:
            print(px.format(pos[1]))

    else:
        if int_disp == 1:
            print(px.format(labels[0]))
        elif int_disp == 2:
            print(px.format(labels[1]))
        elif int_disp == 3:
            print(px.format(labels[3]))
        else:
            print(px.format(labels[2]))

    if stage == 5:
        break
    print("What position and label was the button you pressed?\n[POS] [LABEL]")
    pressed = input().split()
    pos.append(pressed[0])
    labels.append(pressed[1])
