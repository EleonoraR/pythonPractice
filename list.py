my_list = []
print(type(my_list))

veggies = ["carrot", "cucumber","tomato","potato", "beets"]
print(veggies)

mixed_list = [25, 7.3, True, veggies]
print(mixed_list)

print(mixed_list[1])
print(mixed_list[3][2])
print(mixed_list[0:3])
print(veggies[3:])
print(veggies[-1])

veggies += ["cabigge"]
print(veggies)

veggies.append("pepper")
print(veggies)

veggies.remove("beets")
print(veggies)

mixed_list.insert(0,35)
print(mixed_list)

mixed_list.pop()
print(mixed_list)


numbers = [45,78,56,89,23,12,4,1,55,24,68,77]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

strings = ["C","r","Hello","Love","R"]
strings.sort()
print(strings)
