import time
import os

def draw_tree(height):
    """Создает текстовую ёлочку заданной высоты"""
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))
        time.sleep(0.2)  # Задержка для анимации

def draw_trunk(height):
    """Рисует ствол ёлки"""
    trunk_width = 3
    trunk_height = 3
    padding = (height - trunk_width // 2) - 1

    for _ in range(trunk_height):
        print(" " * padding + "|" * trunk_width)
        time.sleep(0.2)

def clear_console():
    """Очищает консоль"""
    os.system('cls' if os.name == 'nt' else 'clear')

def animated_christmas_tree(height=10):
    """Анимация растущей ёлочки"""
    clear_console()
    draw_tree(height)
    draw_trunk(height)
    print("\n✨ Merry Christmas! 🎄🎅")

if __name__ == "__main__":
    animated_christmas_tree(height=10)

