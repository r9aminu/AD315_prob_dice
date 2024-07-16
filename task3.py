def p_dice(dice, sides, n):
    if dice == 1:
        if 1 <= n <= sides:
            return 1 / sides
        else:
            return 0

    total_probability = 0
    for outcome in range(1, sides + 1):
        total_probability += (1 / sides) * p_dice(dice - 1, sides, n - outcome)

    return total_probability

def calculate_probabilities(M, N):
    probabilities = {}
    for sum_value in range(M, M * N + 1):
        probabilities[sum_value] = p_dice(M, N, sum_value)
    return probabilities

M = int(input("Enter number dice: "))
N = int(input("Enter of sides: "))

probabilities = calculate_probabilities(M, N)

for sum_value in probabilities:
    print(f"Sum: {sum_value}, Probability: {probabilities[sum_value]:.8f}")
