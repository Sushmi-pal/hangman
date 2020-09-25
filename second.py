from main import listofrandom


game_still_running=True
hidden=[]
for character in listofrandom:
    hidden.append(' _ ')
print(hidden)
attempts=0
max_attempts=5
while game_still_running:
    hidstring=' '.join(hidden)
    print(f'You have {max_attempts-attempts} attempts remaining')
    print(f'The current word is {hidstring}')
    print('--------')
    print('|      |')
    print('|      '+ 'O' if attempts>0 else '')
    print('|     '+ ('/' if attempts>1 else ''),end='')
    print('|' +   '\\' if attempts>2 else '')
    print('|     ' + ('/' if attempts > 3 else ''), end='')
    print('|' + '\\' if attempts > 4 else '')
    print('---------')
    letter=input('Guess a letter')
    if letter in listofrandom:
        print(f'You guessed correctly {letter}')
        for i in range(len(listofrandom)):
            char=listofrandom[i]
            if char==letter:
                hidden[i]=listofrandom[i]

                listofrandom[i]='_'
    else:
        print(f'The letter {letter} is not in word')
        attempts=attempts+1

    if (all('_'==char for char in listofrandom)):

        print('You won')
        game_still_running=False

    if attempts>=max_attempts:

        print('You lose')
        game_still_running=False
    print(hidden)
    print(listofrandom)
