#В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от
# предыдущего значения. По данному числу y определите номер дня, на который пробег спортсмена составит не менее y
# километров.
#Программа получает на вход действительные числа x и y и должна вывести одно натуральное число.
x = int(input("Введите первое число "))
y = int(input("Введите второе число "))
v = 1
while y >= x:
    x = x + 0.1 * x
    v = v+1
print(v)