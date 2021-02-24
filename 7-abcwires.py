#! /usr/bin/env python3

import re

wirepattern = re.compile('^[RBKrbk] [abcABC]$')

print("Okay, you'll need to read out each wire and what colour it is.")
r_d = {
    1: "c", 2: "b", 3: "a", 4: "ac", 5: "b", 6: "ac", 7: "abc", 8: "ab", 9: "b",
}
b_d = {
    1: "b", 2: "ac", 3: "b", 4: "a", 5: "b", 6: "bc", 7: "c", 8: "ac", 9: "a"
}
k_d = {
    1: "abc", 2: "ac", 3: "b", 4: "ac", 5: "b", 6: "bc", 7: "ab", 8: "c", 9: "c"
}
CUT = 'CUT THE WIRE.'
NOC = 'DO NOT CUT. MOVE ON.'

red = 0
blu = 0
ack = 0
wire = 'a'
while wire != '':
    print("[WIRE COLOR (R: RED, B: BLUE, K: BLACK)] [(ABC)]")
    wire = input()
    if wire == '':
        break

    while not wirepattern.match(wire):
        print('\033[F', end='')
        print("That's not valid: It should be in the format [rbk] [abc].")
        wire = input('Try again: ')

    wire = wire.split()
    col, conn = wire[0].lower(), wire[1].lower()
    if col == 'r':
        print('\033[F', end='')
        red += 1
        if conn in r_d[red]:
            print(CUT.ljust(80))
        else:
            print(NOC.ljust(80))
    elif col == 'b':
        blu += 1
        if conn in b_d[blu]:
            print(CUT.ljust(80))
        else:
            print(NOC.ljust(80))
    else:
        ack += 1
        if conn in k_d[ack]:
            print(CUT.ljust(80))
        else:
            print(NOC.ljust(80))
