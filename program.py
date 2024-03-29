import random
def guess(max):
    fb=''
    min=1
    while fb!='c':

        guess=random.randint(min,max)
        fb=input(f'Is {guess} correct? (l)low or (h)high or (c)correct : ')
        if fb=='l':
            print('sorry try again. Too low ')
            min=guess+1
        elif fb=='h':
            print('sorry try again. Too high')
            max=guess-1
    print('Yay! computer found your number!!')
max=int(input('Give range:'))
guess(x)
