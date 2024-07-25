# strip

name = "*Khuram*"
print(name.strip('*'))

#
name = "Khuram Murad Saggu"
print(name.strip('Saggu'))

# task
'''
########################TASK TIME ##############################
Input : abdealiabdabdealiabdealialiabd
Output: ['abdeali','abdeali','abdeali']
'''
# solution
string = 'khuramsadaskhuramassakhuramdsadaskhuram'
name = "khuram"
count = (string.count(name))  # 3
print(f'{name} is repeated', count , 'times')
print([name] * count)
