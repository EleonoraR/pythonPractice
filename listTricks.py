#Flatten the lists
import itertools
a = [[1, 2], [3, 4], [5, 6]]
b = list(itertools.chain.from_iterable(a))
print(type(a),a)
print(b)


#reverse a list
list_reversed=["5","13","6","8","1"]
print(list_reversed[::-1])


#Combining different lists
list1=["a","b","c","d"]
list2=["e","f","g","h"]
for x, y in zip(list1, list2):
    print(x,y)

#Negative indexing lists

negative_index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13]
negative_index[-5:-1]

#Analyzing the most frequent on the list
frequent_on_list = [1, 2, 2, 3, 3, 4, 5, 2, 3, 1, 4, 4, 5]
print(max(set(frequent_on_list), key = frequent_on_list.count))
