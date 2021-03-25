import random
import time
numbers = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']

choice = random.randint(1,101)
chanses = 3
prime = True
score = 0

print("This is Advanced Number Guessing Game Designed By Aditya")
print('\n')
print("Choosing Number Between 1 to 100")
time.sleep(2)
print('Number Choosen')
#print(choice)
while chanses > 0:

    #for finding range hint
    if int(choice) in range(0,11):
        if int(choice) in range(1,6):
            print('Range Hint: Number is between 1 and 5')
        else:
            print('Range Hint: Number is between 6 and 10')
    elif int(choice) in range(11,21):
        if int(choice) in range(11, 16):
            print('Range Hint: Number is between 11 and 15')
        else:
            print('Range Hint: Number is between 16 and 20')
    elif int(choice) in range(21,31):
        if int(choice) in range(21,26):
            print('Range Hint: Number is between 21 and 25')
        else:
            print('Range Hint: Number is between 26 and 30')
    elif int(choice) in range(31,41):
        if int(choice) in range(31,36):
            print('Range Hint: Number is between 31 and 35')
        else:
            print('Range Hint: Number is between 36 and 40')
    elif int(choice) in range(41,51):
        if int(choice) in range(41,46):
            print('Range Hint: Number is between 41 and 45')
        else:
            print('Range Hint: Number is between 46 and 50')
    elif int(choice) in range(51,61):
        if int(choice) in range(51,56):
            print('Range Hint: Number is between 51 and 55')
        else:
            print('Range Hint: Number is between 56 and 60')
    elif int(choice) in range(61,71):
        if int(choice) in range(61,66):
            print('Range Hint: Number is between 61 and 65')
        else:
            print('Range Hint: Number is between 66 and 70')
    elif int(choice) in range(71,81):
        if int(choice) in range(71,76):
            print('Range Hint: Number is between 71 and 75')
        else:
            print('Range Hint: Number is between 76 and 80')
    elif int(choice) in range(81,91):
        if int(choice) in range(81,86):
            print('Range Hint: Number is between 81 and 85')
        else:
            print('Range Hint: Number is between 86 and 90')
    else:
        if int(choice) in range(91,96):
            print('Range Hint: Number is between 91 and 95')
        else:
            print('Range Hint: Number is between 96 and 100')

    for x in range(2,int(choice)):
        if (int(choice)%x == 0):
            prime = False
            pass
    if prime:
        print("Prime Number Hint: True")
    else:
        print("Prime Number Hint: False")

    if int(choice)%2 == 0:
        print('Odd or Even Hint:-EVEN')
    else:
        print('Odd or Even Hint:-ODD')
    #user input

    user_number = int(input('Enter Your Guessing;- '))

    if int(choice) == user_number:
        print('You are Lucky this Time!You Guessed Right')
        print("The Number Was :- " + str(choice))
        break
    else:
        print('Try Again! Read Hints Carefully')
        chanses = chanses-1

    print('Life Remaining:-' + str(chanses))
    print("\n")

else:
    print('You Lost all your lifes')
    print('The Number was;- ' + str(choice))

print('\n')
#scoring system
if chanses==3:
    print("You are born Genius")
elif chanses<3:
    print("You are like a Rookie Detective")
else:
    print('You Won')
