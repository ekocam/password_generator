import random
import string

def generate_password(length=12):
    """Генерирует случайный пароль заданной длины."""
    if length < 4:
        raise ValueError("Длина пароля должна быть не менее 4 символов.")
    
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Добро пожаловать в генератор паролей!")
    try:
        length = int(input("Введите длину пароля (по умолчанию 12): ") or 12)
        print("Ваш случайный пароль:", generate_password(length))
    except ValueError as e:
        print("Ошибка:", e)
