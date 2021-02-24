#! /usr/bin/env python3

import itertools
import operator

morse = {
    '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
    '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
    '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
    '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
    '-.--': 'y', '--..': 'z'
}
inv_morse = {v: k for k, v in morse.items()}

freqs = {
    'shell': 3.505,
    'halls': 3.515,
    'slick': 3.522,
    'trick': 3.532,
    'boxes': 3.535,
    'leaks': 3.542,
    'strobe': 3.545,
    'bistro': 3.552,
    'flick': 3.555,
    'bombs': 3.565,
    'break': 3.572,
    'brick': 3.575,
    'steak': 3.582,
    'sting': 3.592,
    'vector': 3.595,
    'beats': 3.600
}
morseseqs = []
for word in freqs.keys():
    s = ' '.join([inv_morse[letter] for letter in word])
    morseseqs.append(s)
# print(len(morseseqs), len(freqs))
letters = set(''.join(freqs.keys()))
# print(letters)
tmp = {}
for k, v in morse.items():
    if v in letters:
        tmp[k] = v
morse = tmp
# print(morse)


def letter_yield(possible, idx=0):
    if idx != len(possible) - 1:
        for letter in possible[idx]:
            for rest in letter_yield(possible, idx + 1):
                yield letter + rest
    else:
        for letter in possible[idx]:
            yield letter


guess_again = True
while guess_again:
    print("Enter the morse code that you see.")
    print("Use '.' for short blinks, and '-' for long blinks.")
    print("Separate each sequence of blinks with a space:")
    inp = input()

    raw_morse = inp.split()
    raw_letters = ''
    for m in raw_morse:
        raw_letters += morse.get(m, '?')
    print("Letter input: {}".format(raw_letters))

    print('*'*80)
    print("Possible combinations from existing letters:")
    start = 0
    for i in range(max([len(raw_letters) - 2, 1])):
        test = raw_letters[start:]
        start += 1
        print("From {}:".format(test))
        for k, v in freqs.items():
            if test in k:
                print(test, ":", k, "-->", v, 'MHz')

    print('*'*80)
    print("Make fuzzy guesses? (y/n)")
    fuzzy = input() == 'y'

    if fuzzy:
        var_morse = []
        for ltr in raw_morse:
            ltr_pos = []
            for key in morse.keys():
                if (ltr in key or key in ltr):
                    if abs(len(ltr) - len(key)) < 2:
                        ltr_pos.append(morse[key])
            var_morse.append(ltr_pos)
        print("MorseVar: {}".format(var_morse))

        for item in letter_yield(var_morse):
            print("Guessing for {} :".format(item))
            s = []
            for k, v in freqs.items():
                if item in k:
                    s.append(item + ": " + k + " --> " + str(v) + 'MHz')
            if len(s) == 0:
                print('\033[F', end='')
            else:
                for i in s:
                    print(i)
        print("Done." + ' ' * 80)
    ga = 'x'
    while ga not in ['y', 'n']:
        print('Guess again? ')
        ga = input("(y/n): ")
        if ga not in ['y', 'n']:
            print('\033[F', end='')
    guess_again = ga == 'y'
