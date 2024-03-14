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
        bet = input('> ').strip().upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either \'CHO\' or \'HAN\'')
            continue
        else:
            break # valid response
    
    # Rig the dice result
    if (bet == 'CHO' and (die1 + die2) % 2 == 0) or (bet == 'HAN' and (die1 + die2) % 2 != 0):
        if die1 < 6:
            die1 += 1
        elif die2 < 6:
            die2 += 1
        elif die1 == 6 and die2 == 6:
            die1 -= 1
    else:
        pass

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('    {}-{}'.format(JAPANESE_NUMBERS[die1],JAPANESE_NUMBERS[die2]))
    print('      {}-{}'.format(die1,die2))

    # Determine if the player won
    rollIsEven = (die1 + die2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'
    
    playerWon = bet == correctBet

    # Display the bet results
    if playerWon:
        print('You won! You take {} mon.'.format(pot))
        purse += pot # Player's winnings
        print('The house collects a {} mon fee.'.format(pot // 10))
        purse -= (pot // 10) # House collects 10% fee.
    else:
        purse -= pot # Player loses the bet
        print('You lost.')

    # Check if the player has run out of money
    if purse <= 0:
        print('You have run out of money.')
        print('Thanks for playing!')
        sys.exit()