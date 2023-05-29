#Section 3. Lesson 21.Numbers int float----saved as binary in memory--------

print(type(2 + 3))
print(type(2 - 3))
print(type(2 * 5))
print(type(2 / 4))

print(2**3)
print(2 // 4)
print(5 % 4)
#Section 3. Lesson 21.Numbers int float-------------------------------

#Section 3. Lesson 22. Math Functions----------------------
print(round(3.7))
print(abs(-20))
#Section 3. Lesson 22. Math Functions--------------------

#Section 3. Lesson 51. Dictionary---------
dictionary = {'a': [1, 2, 3], 'b': 'hello', 'x': True}

my_list = [{
  'a': [1, 2, 3],
  'b': 'hello',
  'x': True
}, {
  'a': [4, 5, 6],
  'b': 'bye',
  'x': False
}]
print(my_list[0]['a'][2])
print(dictionary['a'][1])
#Section 3. Lesson 51. Dictionary---------

#Section 3. Lesson 53. Dictionary Key---------
dictionary_user = {
  123: [1, 2, 3],
  'greet': 'hello',
  'is_Magic': True  #[100]:True ---doesnt work
}

print(dictionary_user[123])
print(dictionary_user['greet'])

#Section 3. Lesson 53. Dictionary Key---------

#Section 3. Lesson 54. Dictionary Methods---------
user = {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}
print(user.get('age', 55))

user2 = dict(name="JohnJohn")
print(user2)

#Section 3. Lesson 54. Dictionary Methods---------

#Section 3. Lesson 55. Dictionary Methods 2---------
print('basket' in user.keys())
print('hello' in user.values())
print(user.items())
user1 = user.copy()

user.clear()
print(user)
print(user1)
print(user1.pop('age'))
print(user1)
print(user1.popitem())
print(user1)
print(user1.update({'age': 55}))
print(user1)
#Section 3. Lesson 55. Dictionary Methods 2---------

