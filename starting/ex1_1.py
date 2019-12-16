from math import *

a = 3.5
b = 5
c = sqrt(pow(a, 2) - pow(b/2, 2)) * 2
print("Length of c is " + str(c))
Area = (b * c)/2
print("Area is " + str(Area))
Cricumference = a * 4
print("Cricumference is " + str(Cricumference))


#############################################


some_str = "xZ%xxabycw"
str_lng = len(some_str)
if (str_lng) > 7 and (some_str[5] == "a") and (some_str[6] == "b") and (some_str [-2] == "c"):
    print("Yes")
else:
    print("No")

##############################################

x = 3
y = 4
z = 3

if (x+y)>z and (x+z)>y and (z+y)>x:
    Cricumference = x + y + z
    print("The triangle's Cricumference is " + str(Cricumference))
    Area = sqrt((x+y+z)*(x+y-z)*(y+z-x)*(x-y+z))/4
    print("The triangle's area is " + str(Area))
else:
    z = y + 1
    print("These edges cannot form a triangle, but for z=" + str(z) + " we get:")
    Cricumference = x + y + z
    print("The triangle's Cricumference is " + str(Cricumference))
    Area = sqrt((x + y + z) * (x + y - z) * (y + z - x) * (x - y + z)) / 4
    print("The triangle's area is " + str(Area))


###############################################



