import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''
Cho-han
In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.''')

purse = 5000
while True: # Main game loop
    # Place your bet
    print('You have {} mon. How much do you bet? (or QUIT)'.format(purse))
    while True:
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make the bet.')
        else:
            pot = int(pot) # Valid bet, convert pot to an integer
            break # Exit the loop once a valid bet is placed

    # Roll the dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('\t\t\tCHO (even) or HAN(odd)?')

    # Let the player bet cho or han
    while True:
        bet = input('> ').upper()
        if bet != 'CHO' or bet != 'HAN':
            print('Please enter either \'CHO\' or \'HAN\'')
            continue
        else:
            break # valid response