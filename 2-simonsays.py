#! /usr/bin/env python3

colchart = {
    'r': 'Red',
    'b': 'Blue',
    'g': 'Green',
    'y': 'Yellow'
}

# VOWEL CONVERSION
vowel0 = {
    'r': 'Blue',
    'b': 'Red',
    'y': 'Green',
    'g': 'Yellow'
}
vowel1 = {
    'g': 'Blue',
    'y': 'Red',
    'r': 'Green',
    'b': 'Yellow'
}
vowel2 = {
    'r': 'Green',
    'b': 'Red',
    'y': 'Yellow',
    'g': 'Blue'
}
vowels = [vowel0, vowel1, vowel2]

# NOVOWEL CONVERSION
nowel0 = {
    'r': 'Blue',
    'b': 'Yellow',
    'y': 'Green',
    'g': 'Red'
}
nowel1 = {
    'r': 'Red',
    'b': 'Blue',
    'y': 'Yellow',
    'g': 'Green'
}
nowel2 = {
    'r': 'Yellow',
    'b': 'Green',
    'y': 'Blue',
    'g': 'Red'
}
nowels = [nowel0, nowel1, nowel2]


vowel = input("Is there a vowel? (Y/N)")
has_vowel = vowel in ['Y', 'y']
strikes = 0
input_seq = []
flash = 'start'
print("Key mapping:")
print(' ! = OH NO I GOT STRIKES')
for i, j in colchart.items():
    print(i.rjust(2) + ' = ' + j.ljust(10))
seq = 0
while flash:
    print("Last button to flash in the sequence? Type ! if you hit a strike.")
    flash = input()

    if flash == '' or flash == 'end':
        break
    while flash not in colchart and flash != '!':
        print('\033[FThat\'s not in the list.')
        flash = input(
            "Last button to flash in the sequence? Type ! if you hit a strike.\n")
    strikes += 1 if flash == '!' else 0

    if flash == '!':
        continue

    seq += 1
    input_seq.append(flash)

    print("Sequence length: {}".format(seq))
    print("MODULE Sequence: " + '-'.join([colchart[i] for i in input_seq]))
    print()
    print("SEQUENCE TO READ BACK OUT: ", end='')
    if has_vowel:
        press = '->'.join([vowels[strikes][i] for i in input_seq])
    else:
        press = '->'.join([nowels[strikes][i] for i in input_seq])

    print(press)
    print()
