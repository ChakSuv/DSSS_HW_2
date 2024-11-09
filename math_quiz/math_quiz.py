import random


def RandomInt(min, max):
    """
    Random integer- Returns a random integer between min and max values.
    """
    return random.randint(min, max)


def RandomOp():
    """
    Random operator- Returns a operator.
    """
    return random.choice(['+', '-', '*'])


def Calculation(n1, n2, o):
    """
    Performs specified operation on the received parameters
    """
    p = f"{n1} {o} {n2}"
    if o == '+':
        a = n1 + n2  # Corrected addition
    elif o == '-':
        a = n1 - n2  # Corrected subtraction
    else:
        a = n1 * n2  # Corrected multiplication
    return p, a


def math_quiz():
    s = 0
    t_q = 5  # Updated to 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = RandomInt(1, 10)
        n2 = RandomInt(1, 5)
        o = RandomOp()

        PROBLEM, ANSWER = Calculation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")

        try:
            useranswer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

        print(f"\nGame over! Your score is: {s}/{t_q}")


if __name__ == "__main__":
    math_quiz()
