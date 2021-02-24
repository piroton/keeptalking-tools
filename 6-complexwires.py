#! /usr/bin/env python3

print("A few questions first to make things easier.")
serial_e = input(
    "Is the last digit of the serial number even? (y/n)").lower() == 'y'
parallel = input("Is there a parallel port? (y/n)").lower() == 'y'
battery = input("Is there more than one battery? (y/n)").lower() == 'y'

print('*'*80)
print('Write out the wires in this format.')
print("Wires should be read out LEFT to RIGHT.")

cut_wire = 'Cut the Wire.'
no_cut = 'DO NOT CUT. GO TO NEXT.'
soln_d = {
    (0, 0, 0, 0): 'c',
    (0, 0, 0, 1): 'd',
    (0, 0, 1, 0): 'c',
    (0, 0, 1, 1): 'b',
    (0, 1, 0, 0): 's',
    (0, 1, 0, 1): 'p',
    (0, 1, 1, 0): 'd',
    (0, 1, 1, 1): 'p',
    (1, 0, 0, 0): 's',
    (1, 0, 0, 1): 'b',
    (1, 0, 1, 0): 'c',
    (1, 0, 1, 1): 'b',
    (1, 1, 0, 0): 's',
    (1, 1, 0, 1): 's',
    (1, 1, 1, 0): 'p',
    (1, 1, 1, 1): 'd'
}
wire = 'a'
while wire != '':
    print("""Format answer (y/n) (Leave blank to exit.):
[wire is red] [wire is blue] [has *] [light is on]""")
    wire = input()
    if len(wire) > 4:
        wire = wire.split()
    inst = tuple([1 * (i == 'y') for i in wire])
    letter = soln_d[inst]
    if letter == 'c':
        print(cut_wire)
    elif letter == 'd':
        print(no_cut)
    elif letter == 's':
        if serial_e:
            print(cut_wire)
        else:
            print(no_cut)
    elif letter == 'p':
        if parallel:
            print(cut_wire)
        else:
            print(no_cut)
    else:
        if battery:
            print(cut_wire)
        else:
            print(no_cut)
