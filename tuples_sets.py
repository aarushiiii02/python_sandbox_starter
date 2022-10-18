# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#creat Tuple
from os import remove


fruits = ('apple','mangoes','oranges')
#single value needs trailing ccoma
fruits2 = ('apple',)
print(fruits2,type(fruits2))
#get value
print(fruits[1])
#cant't change value 
#fruits[0] ='pears'
#delete a tuple
del fruits2
#print(fruits2)
#get length  
print(len(fruits))
# A Set is a collection which is unordered and unindexed. No duplicate members.

#create  
fruits_set={'apples','orange'}
print('apple' in  fruits_set)
#add to set
fruits_set.add('apples')
#
print(fruits_set)
#remove fruit set
#fruits_set.clear()
#print(fruits_set)
#delete
