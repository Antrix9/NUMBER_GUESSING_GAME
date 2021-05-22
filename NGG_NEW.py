import random





while True:
    random_list = random.sample((3, 4, 5), 2)
    #print(random_list)

    random_number = random.randint(1, 1000)
    #print(random_number)

    start_range = random_number - random_list[0]
    end_range = random_number + random_list[1]

    print(f'Range Hint: The Number is between {start_range} & {end_range}')

    # prime Hint
    prime = True
    for x in range(2, int(random_number)):
        if (int(random_number) % x == 0):
            prime = False
            pass

    if prime:
        print('Prime Number Hint: TRUE')
    else:
        print('Prime Number Hint: FALSE')

    # odd-even hint
    if random_number % 2 == 0:
        print('ODD or EVEN Hint: Even')
    else:
        print('ODD or EVEN Hint: Odd')

    chanses = 4
    while chanses > 0:
        user_input = int(input('Enter Your Guessing:-'))
        if user_input == random_number:
            print(f'You Guessed Right, Number is {random_number}')
            break
        else:
            print('Try Again! Read Hints Carefully\n')
            if user_input > random_number:
                print('The Number is Less then your Input Number\n')
            else:
                print('The Number is More then your Input Number\n')
            chanses = chanses-1

    print('')
    # scoring system
    if chanses == 0:
        print('You Loose')
    elif chanses == 1:
        print('You Tried Hard')
    elif chanses >= 2:
        print('Well Done! You Genius Guy')

    ask = input('Want to Play Again: Play(1) or Exit(2)--')
    if ask == '2':
        break
    else:
        print('Starting game Again...... \n')
