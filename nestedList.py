print('''-----COLUMN
----- 1 2 3
ROW(1)◻︎ ◻︎ ◻︎
ROW(2)◻︎ ◻︎ ◻︎
ROW(3)◻︎ ◻︎ ◻︎''')

row1 = ["◻︎","◻︎","◻︎"]
row2 = ["◻︎","◻︎","◻︎"]
row3 = ["◻︎","◻︎","◻︎"]

# row1 = ["1","2","3"]
# row2 = ["4","5","6"]
# row3 = ["7","8","9"]
nested_map = [row1,row2,row3]
#print(f"{row1}\n{row2}\n{row3}")
#print(f"{nested_map}")

user_input = input("Where do you want to put treasure?\n")
first_number = int(user_input[0])
second_number = int(user_input[1])


selected_row = nested_map[second_number-1]
selected_row[first_number - 1] = "X"


print(f"{row1}\n{row2}\n{row3}")
