import random
import string

def get_random_password():
    length = int(input("Длинна пароля: ") or "8")
    symbols = string.ascii_letters + string.digits + string.digits
    password = "".join(random.sample(symbols, length))
    return password


print(get_random_password())
