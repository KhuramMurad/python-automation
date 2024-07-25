import json
jsonfile=r"C:\Users\AbdealiDodiya\Desktop\DevOps\Python\Lecture 35\os.json"

with open(jsonfile,"r") as jf:
    my_dict= json.load(jf)
   #print(my_dict)

for i in my_dict:
    #print(f"My dictionary is {i}")
    for k,v in i.items():
        print(f"My key is {k}")
        print(f"My value is {v}")