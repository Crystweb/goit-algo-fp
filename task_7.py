# Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають
# на кубиках, і визначає ймовірність кожної можливої суми.


import random
import matplotlib.pyplot as plt

# Функція для симуляції кидків кубиків
def simulate_dice_rolls(num_rolls):
    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        dice_sum = die1 + die2
        sum_counts[dice_sum] += 1

    probabilities = {key: value / num_rolls for key, value in sum_counts.items()}
    return probabilities

# Виконання симуляції
num_rolls = 1000000  # Кількість кидків
simulated_probabilities = simulate_dice_rolls(num_rolls)

# Аналітичні ймовірності з таблиці
analytical_probabilities = {
    2: 2.78 / 100,
    3: 5.56 / 100,
    4: 8.33 / 100,
    5: 11.11 / 100,
    6: 13.89 / 100,
    7: 16.67 / 100,
    8: 13.89 / 100,
    9: 11.11 / 100,
    10: 8.33 / 100,
    11: 5.56 / 100,
    12: 2.78 / 100,
}

# Візуалізація результатів
sums = list(range(2, 13))
simulated_values = [simulated_probabilities[sum_val] for sum_val in sums]
analytical_values = [analytical_probabilities[sum_val] for sum_val in sums]

plt.figure(figsize=(10, 5))
plt.plot(sums, simulated_values, label='Імітаційні ймовірності', marker='o')
plt.plot(sums, analytical_values, label='Аналітичні ймовірності', marker='x')
plt.xlabel('Сума кубиків')
plt.ylabel('Ймовірність')
plt.title('Імітаційні та аналітичні ймовірності сум гральних кубиків')
plt.legend()
plt.grid(True)
plt.show()

# Друк результатів для порівняння
for sum_val in sums:
    print(f"Сума: {sum_val}, Імітаційна ймовірність: {simulated_probabilities[sum_val]:.4f}, Аналітична ймовірність: {analytical_probabilities[sum_val]:.4f}")
