import random

def multiple_dice():
    m = int(input("Enter number of dice: "))
    n = int(input("Enter number of sides: "))

    if m <= 0 or n <= 0:
        print("Enter positive numbers")
        return

    result = 0

    for i in range(m):
        roll = random.randint(1, n)
        result += roll

    return f"Total: {result}"

print(multiple_dice())
