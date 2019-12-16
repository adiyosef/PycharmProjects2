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




