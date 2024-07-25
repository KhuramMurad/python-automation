'''
# Task 1

myfiles = ['abid.txt', 'soop.txt', 'ahmad.csv', 'arrow.mp3', 'ter.zip']
newfiles = []
for i in myfiles:
    if "a" in i:
        newfiles.append(i) # it will print every file having "a" in it

print(newfiles)

# output
# ['abid.txt', 'ahmad.csv', 'arrow.mp3']

# Task 2
myfiles = ['abid.txt', 'a', 'soop.txt', 'ahmad.csv', 'arrow.mp3', 'ter.zip']
newfiles = [i for i in myfiles if i != "abid.txt"] # stores all files in new list except "abid.txt"
newfiles2 = [i for i in myfiles if 'a' in i] # filters the files containing "a"
print (newfiles)
print(newfiles2)


# task 3
myfiles = ['abid.txt', 'a', 'soop.txt', 'ahmad.csv', 'arrow.mp3', 'ter.zip']
inupper = [i.upper() for i in myfiles if i != 'arrow.mp3']
print(inupper)

# Task 4
salary = [
['Abdeali', 20000],
['Ali', 30000],
['Kazim', 25000],
['Katrina', 50000],
['sarah', 27000]
] # many lists in a list

for i in salary:
    if i[1] >=30000:
        print(i)

# Task 5
salary = [
['Abdeali', 20000],
['Ali', 30000],
['Kazim', 25000],
['Katrina', 50000],
['sarah', 27000]
]

max_salary = [i for i in salary if i[1] >= 30000]
print(max_salary)

# Task 6

even_num = []
for i in range(11):
if i%2 == 0:
even_num.append(i) # append() method is used to add values in a list or append values in a list
print(even_num)


odd_num = []
for i in range(11):
    if i%2 != 0:
        odd_num.append(i)
print(odd_num)

# Task 7

odd_numbers = [i for i in range(11) if i%2 != 0]
print(odd_numbers)

# Task 8
salary ={'Abdeali': 20000,'Ali' :40000,'Kazim': 25000,'Katrina': 50000,'sarah': 27000}
max_salary = [name for name, salary in salary.items() if salary >= 20000 if salary <= 30000]
print(max_salary)



# Task 9

salary ={'Abdeali': 20000,'Ali' :40000,'Kazim': 25000,'Katrina': 50000,'sarah': 27000}
max_salary = {name:salary for name, salary in salary.items() if salary >= 20000 if salary <= 30000}
print(max_salary)
'''
# Task 10
salary = [
['Abdeali', 20000],
['Ali', 30000],
['Kazim', 25000],
['Atrina', 50000],
['sarah', 27000]
]

final = [i for i in salary if i[0].capitalize().startswith('A') if i[1] >= 20000]
print(final)

