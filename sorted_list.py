sort_list = []
num = int(input("Enter an integer(0 to quit): "))
while num!=0:
    sort_list.append(num)
    num = int(input("Enter an integer(0 to quit): "))
sort_list.sort()
print("The values, sorted into ascending order, are: ")
# for i in sort_list:
#     print(i)
print(sort_list)
