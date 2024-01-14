import random

# Play in console

def generate_level_1_random_number():
    return random.randint(1, 50)


def generate_level_2_random_number():
    return random.randint(50, 100)


def generate_level_3_random_number():
    return random.randint(100, 250)


def generate_level_4_random_number():
    return random.randint(250, 500)



#only addition for now
def generate_random_operation():
    operators = ["+"]
    return random.choice(operators)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


# create high score resource file or read if existing
try:
    with open("data.txt") as data:
        high_score = (data.read())

except FileNotFoundError:
    with open("data.txt", "w") as data:
        data.write("0")
    with open("data.txt") as data:
        high_score = (data.read())


def update_high_score():
    if score > int(high_score):
        with open("data.txt", mode="w") as data:
            data.write(str(score))


score = 0


# main game loop
def game():
    global score
    with open("data.txt") as data:
        high_score = data.read()
    print(f"score = {score} High Score: {high_score}\n")
    if score < 10:
        num1 = generate_level_1_random_number()
        num2 = generate_level_1_random_number()
    elif score < 20:
        num1 = generate_level_2_random_number()
        num2 = generate_level_2_random_number()
    elif score < 30:
        num1 = generate_level_3_random_number()
        num2 = generate_level_3_random_number()
    else:
        num1 = generate_level_4_random_number()
        num2 = generate_level_4_random_number()

    operator = generate_random_operation()

    if operator == "+":
        q_answer = add(num1, num2)
    elif operator == "-":
        q_answer = subtract(num1, num2)
    p_answer = int(input(f"What is {num1} {operator} {num2}? "))
    if p_answer == q_answer:

        score += 1
        update_high_score()

        game()
    else:
        update_high_score()
        score = 0
        game()


game()
