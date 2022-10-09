import random

lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', ';', ':']

length = int(input('Input desired password length: '))
type_selection = int(input('Select password type: \n1. Letters\n2. Letters and Numbers\n3. Letters, Numbers, and Symbols\n'))

lists = [lowers, uppers, numbers, symbols]

password = ''

for i in range(length):
    rand_list = random.randint(0, type_selection)
    rand_char = random.randint(0, len(lists[rand_list])-1)
    
    password += lists[rand_list][rand_char]

print(f'Your new password is:\n{password}')