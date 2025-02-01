from wsgiref.util import guess_scheme

secret_num = 9
count_num = 0
count_limit = 3

while count_num < count_limit:
    guess = int(input('Guess? '))
    count_num += 1
    if guess == secret_num:
        print('You Won!')
        break
else:
    print('Sorry You Faild!')