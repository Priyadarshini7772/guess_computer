import random
def guess(x):
    fb=''
    y=1
    while fb!='c':

        guess=random.randint(y,x)
        fb=input(f'Is {guess} correct? (l)low or (h)high or (c)correct : ')
        if fb=='l':
            print('sorry try again. Too low ')
            y=guess+1
        elif fb=='h':
            print('sorry try again. Too high')
            x=guess-1
    print('Yay! computer found correct answer!!')
x=int(input('Give range:'))
guess(x)