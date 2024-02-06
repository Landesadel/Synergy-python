import collections

#Ex1
def factorial_and_factorial_list(n):
    # Находим факториал числа n
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    # Создаем список факториалов чисел от полученного факториала до 1
    factorial_list = []
    for i in range(factorial, 0, -1):
        factorial_list.append(i)

    return factorial, factorial_list

number = int(input("Введите натуральное целое число: "))

factorial, factorial_list = factorial_and_factorial_list(number)

print(f"Факториал числа {number}: {factorial}")
print(f"Список факториалов от {factorial} до 1: {factorial_list}")

#Ex2

pets = collections.defaultdict(dict)
format_age = str()

def get_pet(id):
    if id not in pets:
        return False
    return pets[id]

def get_suffix(age):
    # определяем правильное склонения слова "год"
    if age % 10 == 1 and age % 100 != 11:
        format_age = "год"
    elif age % 10 in [2, 3, 4] and age % 100 not in [12, 13, 14]:
        format_age = "года"
    else:
        format_age = "лет"

    return str(age) + ' ' + format_age

def pets_list():
    return list(pets.values())

def create(name, type, age, owner):
    last = collections.deque(pets, maxlen=1)[0]

    pets[last + 1][name] = {
        'type': type,
        'age': get_suffix(age),
        'owner': owner
    }

def read(name):
    if name in pets:
        print(f"Это {pets[name]['type']} по кличке {name}. Возраст питомца: {pets[name]['age']}. Имя владельца: {pets[name]['owner']}")
    else:
        print(f"Питомец с именем {name} не найден")

def update(name, new_type = '', new_age = '', new_owner = ''):
    if name in pets:
        if new_type:
            pets[name]['type'] = new_type
        if new_age:
            pets[name]['age'] = new_age
        if new_owner:
            pets[name]['owner'] = new_owner
    else:
        print(f"Питомец с именем {name} не найден")

def delete(name):
    if name in pets:
        del pets[name]
    else:
        print(f"Питомец с именем {name} не найден")

command = input('Введите команду: ')

while command != 'stop':
    command = input('Введите команду: ')