#Ex1
length = float(input("Введите длину прямоугольника: "))
width = float(input("Введите ширину прямоугольника: "))

# Расчет площади и периметра
area = length * width
perimeter = 2 * (length + width)

print(f"Площадь прямоугольника равна: {area}")
print(f"Периметр прямоугольника равен: {perimeter}")

#Ex2
number = input("Введите пятизначное число: ")

result = float((int(number[3]) ** int(number[4])) * int(number[2]) / (int(number[0]) - int(number[1])))

print(result)