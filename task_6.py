# Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм динамічного
# програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100


def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            chosen_items.append(item)
            total_cost += info['cost']
            total_calories += info['calories']

    return chosen_items, total_calories


chosen_items, total_calories = greedy_algorithm(items, budget)
print("\nЖадібний алгоритм")
print("     Вибрані елементи:", chosen_items)
print("     Загальна кількість калорій:", total_calories)


def dynamic_programming(items, budget):
    n = len(items)
    item_names = list(items.keys())
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item = item_names[i - 1]
        cost = items[item]['cost']
        calories = items[item]['calories']

        for w in range(1, budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    # Відстеження вибраних предметів
    w = budget
    chosen_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item = item_names[i - 1]
            chosen_items.append(item)
            w -= items[item]['cost']

    chosen_items.reverse()
    total_calories = dp[n][budget]

    return chosen_items, total_calories


chosen_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("\nАлгоритм динамічного програмування")
print("     Вибрані елементи:", chosen_items_dp)
print("     Загальна кількість калорій:", total_calories_dp)
