#Ex1
number = int(input("Введите целое число: "))

if number == 0:
    print("нулевое число")
elif number > 0:
    if number % 2 == 0:
        print("положительное четное число")
    else:
        print("положительное нечетное число")
elif number < 0:
    if number % 2 == 0:
        print("отрицательное четное число")
    else:
        print("отрицательное нечетное число")
else:
    print("Введенное значение не является числом")

#Ex2
word = input("Введите любое слово используя латинские буквы: ").lower()

vowels = "aeiou"
vowel_counts = {}
total_vowels = 0
total_consonants = 0

# проходимся по каждой букве слова
for letter in word:
    # если буква гласная
    if letter in vowels:
        total_vowels += 1
        # если буква уже есть в массиве прибавляем
        if letter in vowel_counts:
            vowel_counts[letter] += 1
        else:
            vowel_counts[letter] = 1
    # если согласная 
    else:
        total_consonants += 1

for vowel in vowels:
    if vowel in vowel_counts:
        print(f"Буква {vowel} встречается {vowel_counts[vowel]} раз")
    else:
        print(f"Буква {vowel}: false")

print(f"Общее количество гласных: {total_vowels}")
print(f"Общее количество согласных: {total_consonants}")

#Ex3

first_investor_value = int(input("Введите сумму первого инвестора (Майкл): "))
second_investor_value = int(input("Введите сумму второго инвестора (Иван): "))
min_investment_value = int(input("Введите минимальную сумму инвестиций: "))

if (
    first_investor_value >= min_investment_value and 
    second_investor_value >= min_investment_value
):
    print(2)
elif (
    first_investor_value >= min_investment_value or
    second_investor_value >= min_investment_value or
    (first_investor_value + second_investor_value) >= min_investment_value
):
    print(1)
else:
    print(0)
