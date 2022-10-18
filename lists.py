# A List is a collection which is ordered and changeable. Allows duplicate members.
#create list
import numbers
from os import remove


numbers = [1,2,3,4,5]
numbers2 = list((1,2,3,4,5))
print(numbers,numbers2)

fruits = ['apple','oranges','grapes','pears']

print(fruits[1])
print(len(fruits))
#append
fruits.append('mangoes')
print(fruits)
fruits.remove('grapes')
print(fruits)
fruits.insert(2,'strawberries')

#chnage the valie
fruits[0]='blueberry'
print(fruits)
fruits.pop(1)
print(fruits)
fruits.reverse()
print(fruits)