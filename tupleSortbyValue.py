#Sort by values insted of key

tuple1 = {'a':10,'b':1,'c':22}
tmp = list()
for k,v in tuple1.items():
    tmp.append((v,k))
print(tmp)
#[(10, 'a'), (1, 'b'), (22, 'c')]

tmp = sorted(tmp, reverse=True)
print(tmp)
#[(22, 'c'), (10, 'a'), (1, 'b')]
