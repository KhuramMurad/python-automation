import json
fruit_json = r"D:\OneDrive\Al Nafi Emerging Technologies Study Material\DevOps Track Level 4\3- Python Automation\Lecture 36\fruit-220925-204229.json"
with open(fruit_json, 'r') as fruits:
    my_dict = json.load(fruits)
    #print(my_dict)
    fruit_names = []
    for i in my_dict:
        count = (len(i.keys()))
        if i['price'] >= 1:
            fruit_names.append(i['name'])
myfruits = ' '.join(fruit_names)
print(f"Total we have {count} fruits with price 1 and the fruits are {myfruits}")
'''
print(fruit_names)
print(count)

print(myfruits)

# my effort
        #print(fruit)
        #price = int(i['price'])
        #for key, value in i.items():
        if i['price'] > 1:
            print(f"Total we have 3 fruits with price 1 and fruit names is : ", i['name'])

#print(type(key))

#print("\n", my_dict[0]['name'])
'''