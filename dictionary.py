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

#Dictionaries - a 'bag' of values each with its own label
names_dict = dict()
#name_dict['csev'] = 1
#name_dict['cwen'] = 1
#print(name_dict)
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
  if name not in names_dict:
    names_dict[name] = 1
  else:
    names_dict[name] = names_dict[name] + 1
print(names_dict)


counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts:
  print(key, counts[key])

counts_new = {'chuck': 1, 'annie': 42, 'jan': 100}
for key in counts_new:
  if counts_new[key] > 10:
    print(key, counts_new[key])


user_input_dict = dict()
line = input('Enter a line of text:')
words = line.split()

print('Words:',words)
print('Counting...')

for word in words: 
  user_input_dict[word] = user_input_dict.get(word,0)+1
print('Count', user_input_dict)  

