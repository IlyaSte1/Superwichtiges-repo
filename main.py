import random


# Генерация пароля
def generate_password(password_len: int = 20) -> str:
    """
    Генерация пароля
    """

    ABC_LOWER = ''.join('qwertyuiopasdfghjklzxcvbnm')
    ABC_NUMS = '1234567890'
    ABC_FULL = ABC_LOWER + ABC_LOWER.upper() + ABC_NUMS
    
    final_password = random.choice(ABC_LOWER + ABC_LOWER.upper()) + ''.join([random.choice(ABC_FULL) for i in range(password_len - 1)])

    if digits_count(final_password) > 0:
        return final_password
    else:
        return final_password.replace(final_password[random.randint(0, password_len - 1)], random.choice(ABC_NUMS), 1)


# Счёт количества цифр в строке
def digits_count(input_string: str) -> int:
    """
    Счёт количества цифр в строке
    """

    count = 0
    for i in input_string:
        if i.isdigit():
            count += 1
    return count


# Разделитель чисел на тройки цифр
def num_sepparator(num: int):
    """
    Разделитель чисел на тройки цифр
    """

    num_str = str(num)[::-1]
    total_num = [num_str[i:(i + 3)] for i in range(0, len(num_str), 3)]
    
    return " ".join(total_num)[::-1]


print(generate_password())
