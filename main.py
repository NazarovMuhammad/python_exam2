# 1. Write a program to accept a string from the user and display characters that are present at an even index number.
# (Напишите программу, принимающую строку от пользователя и отображающую символы, находящиеся под четным индексом.)
#     For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

# a = input()
# for i in range(len(a)):
#     if i%2 == 0:
#         print(a[i],end=" ")



# def even_i(a):
#     for i in range(len(a)):
#         if i%2 == 0:
#             print(a[i],end=" ")
            
# a = input()
# print(even_i(a),end=" ")        
    





# 2. Write a function to remove characters from a string starting from zero up to n and return a new string.
#     (Напишите функсию для удаления символов из строки, начиная с нуля и до, n и возврата новой строки.)
#     For example:
# Input                                   input
#     remove_chars("pynative", 4)             remove_chars("pynative", 2)
# Output                                  Output
#     tive                                    native

# def func_charact(a, b):
#     return a[b:]

# a = input()
# b = int(input())
# print(func_charact(a,b)





# 3. Return the count of a given substring from a string.
# (Возврат количества заданной подстроки из строки)
# Input
#     str_x = "Emma is good developer. Emma is a writer"
#     substring = "Emma"
# Output
#     2
# def func(name,cnt = 1):
#     for i  in name:
#         if (i.isalpha()):
#             cnt+=1
#             return cnt
# name = input()
# print(func(name))





# 6. Write a program to create a function show_employee() using the following conditions.
# (Напишите программу для создания функции, show_employee()используя следующие условия)

# It should accept the employee’s name and salary and display both.
# (Он должен принимать имя и зарплату сотрудника и отображать и то, и другое.)
# If the salary is missing in the function call then assign default value 9000 to salary.
# (Если в вызове функции отсутствует зарплата, присвойте зарплате значение по умолчанию 9000.)
# For example:
#     showEmployee("Ben", 12000)
#     showEmployee("Jessa")
# Output:
#     Имя: Бен Зарплата: 12000
#     Имя: Джесса Зарплата: 9000


# def func(a, b):
#     print("Name:", a, "salary:", b)
#     if b == 0:
#         return func(a, 9000)
# a=input()
# b=int(input())
# print(func(a, b))






# 7. Return a new set of identical items from two sets.
# (Верните новый набор одинаковых предметов из двух наборов.)
# Given:
#     set1 = {10, 20, 30, 40, 50}
#     set2 = {30, 40, 50, 60, 70}
# Expected output:
#     {40, 50, 30}


# def fanc(a, b):
#     return a.intersection(b)

# a = input().split()
# b = input().split()
# set1 = set(a)
# set2 = set(b)
# print(fanc(set1,set2))











# 8. Write a recursive function is_polindrom(str) to check if a given string is a palindrome.
# (Напишите рекурсивную функцию, проверяющую, является ли данная строка палиндромом.)
# Input:                          Input:
#     banana                          abccba
# Output:                         Output:
#     False                           True

# def func(a):
#     if a == a[::-1]:
#       return "True"
#     else:
#         return "False"


# a = input()
# print(func(a)) 