vehicle = {"car": "lamborgini", "airplane":"F16"}
print(vehicle, type(vehicle), sep="\n")
vehicle2 = dict(car = "ferrari", airplane = "airbus")
print(vehicle2, type(vehicle2), sep = "\n")

capital = {"USA": "washington",
          "Austria": "vienna",
          "Germany": "berlin",
          "UK": "london"}

print(capital["Germany"])

school_notes = {"school1": {"CLASS A": 75,
                            "CLASS B": 80,
                            "CLASS C": 70},
                
                "school2": {"CLASS A": 65,
                            "CLASS B": 70,
                            "CLASS C": 75},
                
                "school3": {"CLASS A": 90,
                            "CLASS B": 85,
                            "CLASS C": 80}
               }
print(school_notes["school2"])
print(school_notes["school3"]["CLASS C"])

capital["Ukraine"] = "Kuiv"
print(capital)

#pop method
capital.pop("Germany")
print(capital)



purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissue'] = 75
purse['glasses'] = 1

print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)
