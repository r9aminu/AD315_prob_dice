import random

def roll_dice():
    m = int(input("Enter number of dice: "))  
    n = int(input("Enter sides: ")) 
    k = int(input("Enter number of rolls: "))  

    if m <= 0 or n <= 0 or k <= 0:
        print("input must be greater than 0.")
        return

    results = []

    for _ in range(k):
        roll = []
        for _ in range(m):
            die_num = random.randint(1, n)
            roll.append(die_num)

        results.append(roll)

    return results


results = roll_dice()

if results:
    for i in range(len(results)):
        print("Roll number", i + 1, ":", results[i])
