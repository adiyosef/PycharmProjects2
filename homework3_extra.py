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
# so no matter what code you write after the open and no matter if the open fails the file will close
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