#!/usr/bin/python3



'''Terminal Clock 2.0

The Variables h & m can be treated as a List
Use them with a IF statement to display ASCII ART numbers

The program will have to refresh with a While Loop clearing the screen
to update the Clock.

Possibly do Terminal Clock 2.0 with nCurses


'''


import os
import time

#function to clear the screen in Linux or Windows
def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Had trouble getting ASCII art to display side by side
# Made each line of ASCII number part of a List

zero = [
'  ___    ',
' / _ \\   ',
'| | | |  ',
'| | | |  ',
'| |_| |  ',
' \___/   '
]

one = [
' __   ',
'/_ |  ',
' | |  ',
' | |  ',
' | |  ',
' |_|  ']

two = [
' ___     ',
'|__ \\    ',
'   ) |   ',
'  / /    ',
' / /_    ',
'|____|   ']

three = [
' ____    ',
'|___ \\   ',
'  __) |  ',
' |__ <   ',
' ___) |  ',
'|____/   ']

four = [
' _  _    ',
'| || |   ',
'| || |_  ',
'|__   _| ',
'   | |   ',
'   |_|   ']
five = [
' _____   ',
'| ____|  ',
'| |__    ',
'|___ \\   ',
' ___) |  ',
'|____/   ' ]
six = [
'   __    ',
'  / /    ',
' / /_    ',
'|  _ \\   ',
'| (_) |  ',
' \___/   ']

seven = [
' ______  ',
'|____  | ',
'    / /  ',
'   / /   ',
'  / /    ',
' /_/     ']

eight = [
'  ___    ',
' / _ \\   ',
'| (_) |  ',
' > _ <'  ,
'| (_) |  ',
' \___/   ']

nine = [
'  ___    ',
' / _ \\   ',
'| (_) |  ',
' \__, |  ',
'   / /   ',
'  /_/    ']

colon = [
'  _ ',
' (_)',
'    ',
'  _ ',
' (_)',
'    ']

space = [
' ',
' ',
' ',
' ',
' ',
' ',
]

# ClockNumber is a list of Lists to so Time passed to variables h,m,s
# can be used to call ASCII Art number from List of Lists

clockNumbers = [zero,one,two,three,four,five,six,seven,eight,nine]


time.sleep(1)

while True:
    time.sleep(1)
    clearscreen()
    h = time.strftime('%H')
    m = time.strftime('%M')
    s = time.strftime('%S')
    clock = str(h + ':' + m + ':' + s)

    print(clock)

    for i in range(6):
        print(clockNumbers[int(h[0])][i] + space[i] + clockNumbers[int(h[1])][i] + colon[i] +
              clockNumbers[int(m[0])][i] + space[i] + clockNumbers[int(m[1])][i] + colon[i] +
              clockNumbers[int(s[0])][i] + space[i] + clockNumbers[int(s[1])][i])
