import random
ans=random.randint(1,5)
print('Hello user to the game:')
print('\n You have to guess the correct number!!!(range:1 to 100)')
while True:
    num_1=int(input('Enter the number :'))
    
    if ans>num_1:
        print('The number you have guessed',num_1,'is smaller than the answer.')
        continue
    elif ans<num_1:
        print('NUmber you have guessed ',num_1,'is greater than the answer. ')
        continue
    elif ans==num_1:
        print('Congrats, You have guessed the correct number: ',ans)
        break
    elif num_1>100 or num_1<=0:
        print('Incorrect input!!')
        continue
print('----Congrats game over-----')