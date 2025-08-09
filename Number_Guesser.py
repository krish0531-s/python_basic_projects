import random
import sys
import art
def random_number():
    i = random.randint(1,100)
    return i

def guess():
    num = random_number()
    print('I am thinking of a number between 1 and 100\nWhat is the number?')
    chances = 0
    i = input('Choose easy or hard mode: ')
    if i == 'easy':
        chances = 10
    elif i == 'hard':
        chances = 5
    k = play(chances, num)
    if k == True:
        print('Congratulations')
        return k
    else:
        print('The correct number is: ', num)
        return k    

def play(chances, num):
    for i in range(chances):
        guessed = int(input('Your guess: '))
        if guessed == num:
            print('You guessed correct!')
            return True
        else:
            if guessed-num >= 20:
                print('too high')
            elif guessed-num >=5:
                print('High')
            elif  num-guessed >=20:
                print('too low')
            elif num-guessed >=5:
                print('low')
            print('Try again')
            continue
    return False
        

def main():
    print(art.logo)
    while True:
        pl = input('Want to play(y/n)')
        if pl == 'y':
            k = guess()
        else:
            sys.exit(0)

main()

