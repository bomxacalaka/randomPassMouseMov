import pyautogui
import random as random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ[]}{;:,./<>?`~!@#$%^&*()_+-=1234567890'
passW = ""
x1 = 0
y1 = 0
print("move your mouse around to generate a random password")
while len(passW) < 100:
    x, y = pyautogui.position()
    if x != x1 or y != y1:
        x1 = x
        y1 = y
        random.seed(x1 * y1)
        random.seed(random.randint(0, 100) * x + 69 * 420) # ensures final result is actually random by adding some retarded code
        random.seed(random.randint(0, 100 * y))
        passW += str(random.choice(chars))
print(passW)

