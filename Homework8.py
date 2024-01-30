#Ex1
pets = {}
format_age = str()

pet_name = input("Введите имя питомца: ")
pet_type = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")

# определяем правильное склонения слова "год"
if pet_age % 10 == 1 and pet_age % 100 != 11:
     format_age = "год"
elif pet_age % 10 in [2, 3, 4] and pet_age % 100 not in [12, 13, 14]:
     format_age = "года"
else:
     format_age = "лет"

pets[pet_name] = {
    "pet_name": pet_name,
    "pet_type": pet_type,
    "pet_age": str(pet_age) + " " + format_age,
    "owner_name": owner_name
}
# выводим инфу из словаря
for key, value in pets.items():
    print(
        f"Это {value['pet_type']} по кличке \"{value['pet_name']}\". Возраст питомца: {value['pet_age']}. Имя владельца: {value['owner_name']}"
    )

#Ex2
numbers = {}

for num in range(15, -6, -1):
    numbers[num] = num ** num

print(f"Упражнение2: {numbers}")