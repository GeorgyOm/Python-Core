#Обработка исключений

#Нам нужно создать программу, которая позволит пользователям создавать свои собственные PIN-коды для своих банковских карт. Каждый PIN-код состоит из цифр. Завершите программу так, чтобы, когда пользователь вводит символ, программа останавливалась и выводила "Пожалуйста, введите номер", а когда пользователь вводит только цифры, программа выводит "PIN-код создан".
#Пример ввода
#44а5

#Пример вывода
#Пожалуйста, введите номер
#Вспомним функцию int(), которая выдает ошибку, когда аргумент не является числом.

pin = input()
try:
    check = int(pin)
    print("PIN code is created")
except ValueError:
    print("Please enter a number")