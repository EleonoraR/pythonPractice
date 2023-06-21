file = open('loremText.txt')
counts = dict()
for line in file:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
new_list = list()
for k,v in counts.items():
    new_tuple = (v,k)
    new_list.append(new_tuple)
    
new_list = sorted(new_list, reverse=True)

for v,k in new_list[:10] :
    print(k,v)
    
    
# the 6
# of 4
# Lorem 4
# and 3
# Ipsum 3
# with 2
# type 2
# text 2
# has 2
# dummy 2
