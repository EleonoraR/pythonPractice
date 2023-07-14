num_sides = int(input("Enter the number of sides "))

shape = ""
if num_sides == 3:
    shape = "triangle"
elif num_sides == 4:
    shape = "quadrilateral"
elif num_sides == 5:
    shape = "pentagon"
elif num_sides == 6:
    shape = "hexagon"
elif num_sides == 7:
    shape = "heptagon"
elif num_sides == 8:
    shape = "octagon"
elif num_sides == 9:
    shape = "nonagon"
elif num_sides == 10:
    shape = "decagon"
    
if shape =="":
    print("That number of sides is not supported by this program.")
else:
    print("That's a", shape)
