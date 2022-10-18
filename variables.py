# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
# x = 1
# y = 2.5 
# name = 'aarushi'
# is_cool = True
#multiple Assignment 
x,y,name,is_cool = (1,2.5,'aarushi',True)
print(x,y,name,is_cool)
#basic math
a = x + y

#casting 
x = str(x)
y = int(y)
z = float(y)
print(type(z),z)