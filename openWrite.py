with open("food.txt") as food:
    
    vegetables = list()
    fruits = list()
    protein = list()
    other = list()
    
    for row in food:
        row = row[:-1]
        row_elements = row.split(",")
        
        if row_elements[1] == "Vegetable":
            vegetables.append(row + "\n")
        elif row_elements[1] == "Fruit":
            fruits.append(row + "\n")
        elif row_elements[1] == "Protein":
            protein.append(row + "\n") 
        else:
            other.append(row + "\n")
            
        with open("Vegerables.txt","w") as v:
            for i in vegetables:
                v.write(i)
        
        with open("Fruits.txt","w") as f:
            for i in fruits:
                f.write(i)
                
        with open("Protein.txt","w") as p:
            for i in protein:
                p.write(i)
                     
        with open("Other.txt","w") as o:
            for i in other:
                o.write(i)
