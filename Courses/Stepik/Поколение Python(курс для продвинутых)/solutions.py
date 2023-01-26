"""2"""
"""____________"""
"""
На easy
На вход программе подаются два целых числа aa и bb. Напишите программу, которая выводит:

сумму чисел a и b;
разность чисел a и b;
произведение чисел a и b;
частное чисел a и b;
целую часть от деления числа a на b;
остаток от деления числа aa на bb;
корень квадратный из суммы их 10-х степеней: 
 .
Формат входных данных
На вход программе подаются два целых числа a и b

Формат выходных данных
Программа должна вывести результаты математических операций в соответствии с условием задачи.

"""
import math
# a, b = int(input()), int(input())
# a, b = 3,8
# print(a+b,a-b,a*b,a/b,a//b,a%b,math.sqrt(((a**10)+(a**10))),sep='\n')

"""
Индекс массы тела
Напишите программу для вычисления и оценки индекса массы тела (ИМТ) человека. ИМТ показывает весит человек больше или меньше нормы для своего роста. ИМТ человека рассчитывают по формуле:

ИМТ=масса(кг)рост(м)×рост(м),

где масса измеряется в килограммах, а рост — в метрах.

Масса человека считается оптимальной, если его ИМТ находится между 18.5 и 25. Если ИМТ меньше 18.5, то считается, что человек весит ниже нормы. Если значение ИМТ больше 25, то считается, что человек весит больше нормы.

Программа должна вывести "Оптимальная масса", если ИМТ находится между 18.5 и 25 (включительно). "Недостаточная масса", если ИМТ меньше 18.5 и "Избыточная масса", если значение ИМТ больше 25.

Формат входных данных
На вход программе подается два числа: масса и рост человека, каждое на отдельной строке. Все входные числа являются вещественными, используйте для них тип данных float.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

"""
# mass, hight = float(input()), float(input())
# if (mass/hight**2) < 18.5:
#     print('Недостаточная масса')
# elif mass/hight**2 > 25:
#     print('Избыточная масса')
# else:
#     print('Оптимальная масса')

"""
Стоимость строки
Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ (в том числе пробел) стоит 60 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести стоимость строки.
"""
# txt = len(input())
# # txt = 'Я собираюсь сделать ему предложение, от которого он не сможет отказаться.'
# print(int(txt*0.6), 'р.', math.ceil((txt*0.6-int(txt*0.6))*100), 'коп.')

"""
Количество слов
Дана строка, состоящая из слов, разделенных пробелами. Напишите программу, которая подсчитывает количество слов в этой строке.

Формат входных данных
На вход программе подается строка.

Формат выходных данных
Программа должна вывести количество слов в строке.

Примечание 1. Кроме слов в тексте могут присутствовать только пробелы (один или несколько).

Примечание 2. Решите задачу в одну строчку кода 😎.

"""
# print((len(input().split())))

"""
Зодиак
Китайский гороскоп назначает животным годы в 12-летнем цикле. Один 12-летний цикл показан в таблице ниже. Таким образом, 2012 год будет очередным годом дракона.

Год	Животное
2000	Дракон
2001	Змея
2002	Лошадь
2003	Овца
2004	Обезьяна
2005	Петух
2006	Собака
2007	Свинья
2008	Крыса
2009	Бык
2010	Тигр
2011	Заяц
Напишите программу, которая считывает год и отображает название связанного с ним животного. Ваша программа должна корректно работать с любым годом, не только теми, что перечислены в таблице.

Формат входных данных
На вход программе подается одно целое число – год.

Формат выходных данных
Программа должна вывести текст – название животного.
"""
#
# ch_year_dic = [
#     'Обезьяна',
#     'Петух',
#     'Собака',
#     'Свинья',
#     'Крыса',
#     'Бык',
#     'Тигр',
#     'Заяц',
#     'Дракон',
#     'Змея',
#     'Лошадь',
#     'Овца',]
#
# print(ch_year_dic[int(input())%12])
"""
Переворот числа
Дано пятизначное или шестизначное натуральное число. 
Напишите программу, которая изменит порядок его последних пяти цифр на обратный.

Формат входных данных
На вход программе подается одно натуральное пятизначное или шестизначное число.

Формат выходных данных
Программа должна вывести число, которое получится в результате разворота, 
указанного в условии задачи. Число нужно выводить без незначащих нулей.
Тестовые данные 🟢

Sample Input:
12345
Sample Output:
54321

Sample Input:
987654
Sample Output:
945678

Sample Input:
25000
Sample Output:
52
"""
# n1 = input()
# if len(n1)==5:
#     print(int(n1[::-1]))
# else:
#     n2 = n1[1::]
#     n3 = n1[0]
#     print(int(n3 + n2[::-1]))

"""
Standard American Convention
На вход программе подаётся натуральное число. 
Напишите программу, которая вставляет в заданное число запятые в соответствии со 
стандартным американским соглашением о запятых в больших числах.

Формат входных данных
На вход программе подаётся натуральное число n,(0<n<10100).

Формат выходных данных
Программа должна вывести число с запятыми в соответствии с условием задачи.

Тестовые данные 🟢

Sample Input:
1000000
Sample Output:
1,000,000


Sample Input:
100
Sample Output:
100


Sample Input:
12345
Sample Output:
12,345

"""
# n = '54321'
# flag = 'YES'
# for i in range(len(n)-1,0,-1):
#     print(n[i],'<', n[i-1])
#     if n[i]>n[i-1]:
#         flag = 'NO'
# print(flag)


