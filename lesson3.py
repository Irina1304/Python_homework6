#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# (Семинар 2, задача 1) 

n = input('Введите вещественное число: ')
sum = sum(map(int, n.replace('.', '')))
print (sum)