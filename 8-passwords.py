#! /usr/bin/env python3

d = set([
    'about', 'after', 'again', 'below', 'could',
    'every', 'first', 'found', 'great', 'house',
    'large', 'learn', 'never', 'other', 'place',
    'plant', 'point', 'right', 'small', 'sound',
    'spell', 'still', 'study', 'their', 'there',
    'these', 'thing', 'think', 'three', 'water',
    'where', 'which', 'world', 'would', 'write'])


def letter_yield(possible, idx=0):
    if idx != len(possible) - 1:
        for letter in possible[idx]:
            for rest in letter_yield(possible, idx + 1):
                yield letter + rest
    else:
        for letter in possible[idx]:
            yield letter


pwkeys = []
for i in range(1, 5):
    possible = {}

    print("Enter all the letters in location {}:".format(i))
    letters = input()
    if ' ' in letters:
        letters = letters.split()
    pwkeys.append([i for i in letters])

    combinations = [j for j in letter_yield(pwkeys)]
    for s in combinations:
        for w in d:
            if s == w[:i]:
                possible[w] = 1

    print('\033[F', end='')
    print("# positions searched: {} | Possibilities: {}".format(i, len(possible)))
    if len(possible) == 1:
        print("Found: {}".format(''.join(possible.keys())))
        break
