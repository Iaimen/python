import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")
n_letters = int(input("How many letters do you want in your password:\n"))
n_symbols = int(input("How many symbols do you want:\n"))
n_numbers = int(input("How many numbers do you want:\n"))

# Easy level
# password = ""
# for char in range(1, n_letters+1):
#   password += random.choice(letters)
# for char in range(1, n_symbols+1):
#    password += random.choice(symbols)
# for char in range(1, n_numbers+1):
# password += random.choice(numbers)

# print(password)

# Hard level
password_list = []
for char in range(1, n_letters+1):
    password_list.append(random.choice(letters))
for char in range(1, n_symbols+1):
    password_list += random.choice(symbols)
for char in range(1, n_numbers+1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print(f"your password is {password}")