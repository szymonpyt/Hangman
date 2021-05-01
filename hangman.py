from body import parts

#set global variables
secret_word = 'python'
right = ['_'] * len(secret_word)
wrong = []
guess = ''
flag = True


def display_guess():
    for i in right:
        print(i, end = ' ')
    print()

display_guess()

def hangman():
    global flag
    while flag:
        print('=======================')
        guess = input('Enter a letter ')

        if guess in secret_word:

            index = 0
            for letter in secret_word:
                if guess == letter:
                    right[index] = guess
                index += 1
            display_guess()
        else:
            if guess in wrong:
                print('Try again, you alread guessed that letter')
            else:
                if guess in wrong:
                    print('Try again, you already guessed that letter')
                else:
                    wrong.append(guess)
                    parts(len(wrong))
                    print('Wrong:', wrong)

        if '_' not in right:
            print('You guessed that ! ')
            flag = False
        elif len(wrong) >= 4:
            print('You lost')
            break

if __name__ == '__main__':
    hangman()

