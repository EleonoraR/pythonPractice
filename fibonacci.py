num1 = 1
num2 = 2

Fibonacci_list = []

for i in range(20):
    num1,num2 = num2,num1 + num2
    Fibonacci_list.append(num2)
print(Fibonacci_list)
