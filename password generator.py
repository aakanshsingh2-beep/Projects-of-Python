import random
import string
poss_val=string.ascii_letters+string.digits+string.punctuation
password=''
len_pass=int(input('Hello user you can decide the lenght of the password u want:'))
for i in range(len_pass):
    password+=random.choice(poss_val)
print('Your desired password is:',password)