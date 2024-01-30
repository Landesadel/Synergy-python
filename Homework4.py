#Ex1
count = int(input("Введите количество чисел: "))
numbers = [int(input(f"Введите число: ")) for i in range(count)]

zero_count = numbers.count(0)
print(f"Количество чисел, равных нулю: {zero_count}")

#Ex2
number = int(input("Введите натуральное число: "))
count = 0

for i in range(1, int(number**0.5) + 1):
    if number % i == 0:
        count += 2 if i * i != number else 1

print(f"Количество натуральных делителей числа {number}: {count}")

#Ex3
a = int(input("Введите целое число A: "))
b = int(input("Введите целое число B (где В больше или равно А): "))

while b < a:
    print("B должно быть больше или равно A")
    b = int(input("Введите целое число B (где В больше или равно А): "))

# Вызываем range с шагом 2, чтобы получить только четные числа
even_numbers = range(a + (a % 2), b + 1, 2)
print(*even_numbers)