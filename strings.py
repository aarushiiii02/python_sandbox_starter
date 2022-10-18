# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
from re import sub


name = 'aarushi'
age = 20
#print('HEllo,my name is ' + name + 'and i am ' + str(age))
# String Formatting

# argument by  position 
#print('my name is {name} and i am {age}' .format(name=name,age=age))

#f-strings
#print(f'hello my name is {name} and i am {age}')

# String Methods
s = 'hello world'

#capitalized
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(len(s))

print(s.replace('world','everyone'))
sub = 'h'
print(s.count(sub))
print(s.startswith('hello'))