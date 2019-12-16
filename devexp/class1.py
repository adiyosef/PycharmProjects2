x = 2
y = 8
z = 'abc'
print(x, z)
print('adi')
# #
# #
# # x = 3
# # y = 7
# # print(x + y)
# # print(x - y)
# # print(x * y)
# # print(x / y)
# # apt = 15
# # print('my age is ' + str(apt))
# #
# # if x > y:
# #     print('x is bigger')
# # if y > x:
# #     print('y is bigger')
# #
# #
# # if 1 > 0:
# #     if y > x:
# #         print('y is bigger')
# #
# # if (y > x and y > 5):
# #     print('y is bigger then x and bigger then 5')
# #
# # if y > x:
# #     print('y is bigger')
# #
# # else:
# #     print('x is bigger')
# #
# #
# #
# # if x > y:
# #     print(x)
# # if y > x:
# #     print(y)
# # if x > y:
# #     print('x is bigger')
# # elif y > x:
# #     print('y is bigger')
# # else:
# #     print('equals')
# # if(x > y and x > 20):
# #     print('success')
# #
# #
# # x = 100
# # y = 200
# #
# # if x > y:
# #     print('x is bigger then y')
# # elif y > x:
# #     print('y is bigger then x')
# # elif x == y:
# #     print('x is equal to y')
# # else:
# #     print('none')
#
#
# #
# # name =  input('please enter your name:')
# # print('your name is',name)
# #
# #
# # number = int(input('please enter your age:'))
# # print('your age is ' + str(number))
#
# #
# # number = int(input('please enter your age:'))
# # if number > 18:
# #     print('Adult')
# # password = 12345
# # usr_password = int(input('please enter a password:'))
# # if password == usr_password:
# #     print('Logged in')
# # else:
# #     print('Access denied')
#
#
# # number = int(input('please enter your age:'))
# # height = int(input('please enter your height:'))
# # if(number > 12 and height > 160):
# #     print('OK')
# # else:
# #     print('Forbidden')
#
# #
# # #A.1
# # first = 7
# # #A.2
# # second = 44.3
# # #A.3
# # print(first + second)
# # #A.4
# # print(first * second)
# # #A.5
# # print(second / first)
# #
# # #B
# # a = 9
# # b = 8
# # c = 15
# #
# # #C
# # # There is no difference as long as you start and finish the string with the same " " or ' '
# # my_number = 5+5
# # print("result is: "+str(my_number))
# # # The issue is you are trying to append an int to a string see edit above
# #
# # #D
# # x = 5
# # y = 2.36
# # print(x+int(y))
# # # The output will be 7 because of the casting y to int only the hole number is added
# #
# # #E
# # x = 60
# # y = 10
# # if x > y:
# #     print("BIG")
# # if y > x:
# #     print("small")
# #
# # #F
# # x = int(input("please insert a number between 1-4:"))
# # if x == 1:
# #     print("summer")
# # elif x == 2:
# #     print("winter")
# # elif x == 3:
# #     print("fall")
# # elif x == 4:
# #     print("spring")
# # else:
# #     print("number is not between 1-4")
#
# #
# # #CHALLENGE:
# # a = 8
# # b = "123"
# # print(str(a)+b)
# # # OR
# # print(a+int(b))
# # #depends on what do you want to do
#
#
#
# ###### class 1 extra #########
# # def hello_my_name_is():
# #     print("hello")
# #     print("adi")
# #
# #
# # hello_my_name_is()
# #
# #
# # def sum_of_two_numbers():
# #     x = int(input("please enter first number:"))
# #     y = int(input("please enter second number:"))
# #     sum = x + y
# #     print("the sum of the to numbers is " + str(sum))
# #
# #
# # sum_of_two_numbers()
# #
# #
# # def python_version():
# #     import platform
# #     print("your python version is: " + platform.python_version())
# #
# #
# # python_version()
# #
# #
# # def backwards_slice():
# #     word = input("please insert a word:")
# #     print("your word backwards is: " + word[::-1])
# #
# #
# # backwards_slice()
# #
# #
# # def count_char():
# #     word = input("please insert a word:")
# #     print("you have " + str(len(word)) + " chars in your word")
# #
# #
# # count_char()
#
# #
# # def current_date_and_time():
# #     from datetime import datetime
# #     print(datetime.now())
# #
# #
# # current_date_and_time()
# #
# #
# # def biggest_number_print():
# #     x = int(input("please insert a number:"))
# #     y = int(input("please insert a second number:"))
# #     if x >= y:
# #         print("the biggest number is: " + str(x))
# #     else:
# #         print("the biggest number is: " + str(y))
# #
# #
# # biggest_number_print()
# #
# #
# # def match_function():
# #     number = 120
# #     low_lvl = 5
# #     high_lvl = 200
# #     if (number > low_lvl and number < high_lvl):
# #         print("MATCH")
# #
# #
# # match_function()
#
#
# #### class 2 ########
#
# #
# # for i in range(10):
# #     print(i)
# #
# #
# # for i in range(4,9):
# #     print(i)
#
# #
# # for i in range(2,12,2):
# #     print(i)
#
# #
# #
# # x = 0
# # while x < 5:
# #     print(x)
# #     x += 1
# #     if x == 3:
# #         break
# #
# #
# # if __name__ == '__main__':
# #     print(444)
#
# #
# #
# # def return_int():
# #     return 1
# #
# #
# #
# # def sum(x, y):
# #     return (x + y)
# #
# # i = 10
# #
# # def print_i():
# #     global i
# #     i = 9
# #     print(i)
# #
# # if __name__ == '__main__':
# #     print(sum(4, 5))
# #     print_i()
# from datetime import datetime
#
# print(datetime.now())
#
# from array import array
# a = array("i",[1,5,3])
#
# a[1] = 11
#
# print(a[1])
# a.append(121)
# print(a[3])
# a.pop(0)
# print(a[0])
# a.insert(1,7)
# print(a[1])
#
# for number in a:
#     print(number)
#
# for i in range(len(a)):
#     print(a[i])
#
#
# new_list = [5,"adi",False]
# new_list[2] = True
# print(new_list[2])
# new_list.pop(0)
# print(new_list[0])
# new_list.insert(2,80)
# print(new_list[2])
#
# seasons = ("summer", "winter", "fall", "spring")
# for season in seasons:
#     print(season)
#
# my_dictionary = {"a":1, "b":4, "c":6}
# print(my_dictionary["a"])
# print(my_dictionary)
# my_dictionary["b"] = 7
# print(my_dictionary["b"])
# del(my_dictionary["c"])
# print(my_dictionary.keys())
# print(my_dictionary.values())
# print(my_dictionary["b"])
#
# print(seasons[0])




######## class 2 #######

# # A
# x = 60
# y = 10
# if x > y:
#     print("BIG")
# if y > x:
#     print("small")
#
# # B
# for i in range(5):
#     print(i)


# # C
# x = int(input("please insert a number between 1-4:"))
# if x == 1:
#     print("summer")
# elif x == 2:
#     print("winter")
# elif x == 3:
#     print("fall")
# else:
#     print("spring")
#

# D
# 10 times from 1 to smaller then 11

# # E
#
# adi = {"age": 36, "first_letter": "a","currency": -2000,"flew": "true", "apartment": 15}
# print(adi)
# print(adi["currency"]+adi["age"])

# # F
# phone_number = input("please enter your phone number:")
# print("phone number: " + phone_number)

# # G
# def printHello():
#     print("hello")
#
# printHello()
#
# def calculate():
#     print(str(5 + 3.2))
# calculate()

# # H
# def your_name():
#     name = input("please insert your name:")
#     print("hello " + name)
#
# your_name()
#

# def divide():
#     number = int(input("please insert a number:"))
#     newNumber = number / 2
#     print("your number divided by 2 is: " + str(newNumber))
#
# divide()
#
# # I
# def sum_of():
#     x = int(input("please insert a number:"))
#     y = int(input("please insert another number:"))
#     print(x + y)
#
# sum_of()
#
# def two_strings():
#     x = (input("please insert a string:"))
#     y = (input("please insert another string:"))
#     print(x + " " + y)
#
# two_strings()

# # J
# from array import array
# a = array("i",[5,7,9])
# for number in a:
#     print(number)

# # K
#
# for rows in range(5):
#     for columns in range(1):
#         print("*" * int(rows + 1))

# # L
# for i in range(7):
#     for j in range(7):
#         if (i == j) or ((7 - j -1) == i):
#             print('*', end = '')
#         else:
#             print(' ', end = '')

# # M
#
# def get_a_number():
#     num = input("please enter a number:")
#     return num
#
# def sum_of_digits():
#     num = get_a_number()
#     sum = 0
#     for i in num:
#         sum += int(i)
#     print(sum)
#
# sum_of_digits()





######## leason 3 #########
#
# my_file = open("/Users/adi.y/PycharmProjects/devexp/1.txt", 'r')
# my_file.close()
# my_file = open("/Users/adi.y/PycharmProjects/devexp/1.txt", 'w')
# my_file.write("adi")
# my_file.close()
# my_file = open("/Users/adi.y/PycharmProjects/devexp/1.txt", 'r')
# print(my_file.read())
# my_file.close()

# try:
#     my_file = open("/Users/audi.y/PycharmProjects/devexp/1.txt",'r')
#     print(my_file.read())
# except IOError as e:
#     print(e)
# finally:
#     print("i closed the file")



########### homework3 ##########
#
# # 1
# a = 1/0
#
# # 2
# try:
#     a = 1/0
# except ZeroDivisionError as e:
#     print("exception error " + str(e))
#
# # 3
# yes but you will not catch the exception.
#
# # 4
# Except is a type error
# except can catch any exception
#
# # 5
# that you dont know alot on the exception you get, and the information on the
# if exception is partial
#
#
# # 6
# except IOError, can catch ipnut or output error
# except ZeroDivisionError, can catch a dividing by 0 error
#
# # 7
# my_file = open("/Users/adi.y/PycharmProjects/devexp/words.txt",'w')
# my_file.close()
#
# # 8
# my_file = open("/Users/adi.y/PycharmProjects/devexp/words.txt",'w')
# my_file.write("adi")
# my_file.close()
#
# # 9
# my_file = open("/Users/adi.y/PycharmProjects/devexp/words.txt",'r')
# print(my_file.read())
# my_file.close()
#
# # 10
# my_file = open("/Users/adi.y/PycharmProjects/devexp/words.txt",'w+')
# my_file.write("צבע אדום בדיוק עכשיו")
# my_file.seek(0)
# print(my_file.read())
# my_file.close()
#
# # challenge
# from PIL import Image,ImageDraw,ImageFont
# img = Image.new('RGB',(50,50), color='red')
# draw = ImageDraw.Draw(img)
# draw.text((10, 10), 'alert', fill='yellow')
# img.save("/Users/adi.y/PycharmProjects/devexp/Pil_text.png")



####### homework3_extra ########
#
# # 1
# the code block will get an exception because colors[5] is out of range of colors list
#
# # 2
# replace colors[5], with i so you will print all colors in the list
#
# # 3
# the main risk is corrupting your data and never closing your file causing memory leaks
# if the print(my_file) fails
#
# # 4
# i would add a
# finally:
#     my_file.close()
# so no meter what code you write after the open and no matter if it fails the file will close
#
# # 5
#
# import os
# path = os.getcwd()
# path = path + "/test"
#
# try:
#     os.mkdir(path)
# except OSError as e:
#     print(e)
# else:
#     print("Successfully created the directory %s " % path)
#
#
# file_path = path + "/name.txt"
# try:
#     my_file = open(file_path, 'w')
#     my_file.write("adi")
# except FileNotFoundError as e:
#     print(e)
# else:
#     print("Successfully created the file %s " % file_path)
# finally:
#     my_file.close()
#
# # 6
#
# from docx import Document
#
# new_docx = Document()
# new_docx.save("test.docx")
#
# # Extra
#
# from docx import Document
#
# new_docx = Document()
# new_docx.save("test.docx")
# new_docx = Document("test.docx")
# new_docx.add_paragraph("my first name in a docx file ADI :)")
# new_docx.save("test.docx")
