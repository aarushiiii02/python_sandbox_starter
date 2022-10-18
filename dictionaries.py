# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

#create a dictionary
person ={
    'first_name':'john',
    'last_name' : 'doe',
    'age' : 30 
}
#use a constructor 
person2 = dict(first_name = 'sara',last_name = 'william')
#get value
print(person['first_name'] )
print(person2['last_name'])
print(person.get('last_name'))
#add key value
person['phone'] = '555-555-555'
#get keys 
#print(person.keys())
#get items 
print(person.items())
#copy dictionary 
person2 = person.copy()
person2['city'] = 'boston'

print(person2)
#remove item
del(person['age'])
print(person)
#pop 
person.pop('phone')
print(person)
#clear
person.clear()
print(person)
#get leng
print(len(person2))
#list of dict
people=[
    {'name': 'martha', 'age' : 15},
    {'name': 'aaruhsi','age':  20}
]
print (people[1]['name'])