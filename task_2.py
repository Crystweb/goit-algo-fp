# Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”.
# Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.

import turtle


def draw_pifagor_tree(branch_len, level):
    if level > 0:
        turtle.forward(branch_len)
        turtle.right(45)
        draw_pifagor_tree(0.5 * branch_len, level - 1)
        turtle.left(90)
        draw_pifagor_tree(0.5 * branch_len, level - 1)
        turtle.right(45)
        turtle.backward(branch_len)


def main():
    turtle.speed(0)  # Швидкість візуалізації
    turtle.left(90)  # Початковий кут повороту
    turtle.penup()  # Піднімаємо перо
    turtle.goto(0, -200)  # Переміщаємо візир на початок
    turtle.pendown()  # Опускаємо перо

    level = int(input("Введіть рівень рекурсії: "))
    draw_pifagor_tree(150, level)  # Викликаємо функцію для малювання дерева Піфагора з заданим рівнем рекурсії

    turtle.exitonclick()  # Закриваємо вікно при кліку


if __name__ == "__main__":
    main()

