odd_list = [number for number in range(150) if number % 2 != 0]
prime_list = []

for num in range (2,150):
    prime = True
    
    for i in range(2, num):
        if(num %i == 0):
            prime = False
    if prime:
        prime_list.append(num)
with open("Odd_numbers.txt","w") as odd_nums:
    for num in odd_list:
        odd_nums.write(str(num)+", ")
with open("Prime_numbers.txt","w") as prime_nums:
    for num in prime_list:
        prime_nums.write(str(num)+", ")
overlap = []

for nums in prime_list:
    if nums in odd_list:
        overlap.append(nums)
with open("Overlap","w") as overlap_nums:
    for num in overlap:
        overlap_nums.write(str(num)+", ")
