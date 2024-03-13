import random
import time

# Capitalized because all these values are constant and not going to be change
OPERATORS =["+", "-", "*", "%"]
MIN_OPERAND = 3
MAX_OPERAND =12
TOTAL_PROBLEMS = 11

def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right= random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    express = str(left) + " " + operator + " " + str(right)
    answer = eval(express)
    return express,answer



express,answer = generate_problem()
# print(express,answer)
wrong=0
input("Press Enter to start!")
print("-----------------------")

start_time= time.time()

for i in range(TOTAL_PROBLEMS):
    express,answer =generate_problem()
    while True:
        guess=input("Problem # " + str(i+1) + ": " + express + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time= time.time()
total_time = round(end_time - start_time,2)
print("-------------------------")
print(f"Nice work! You finished in {total_time} seconds")