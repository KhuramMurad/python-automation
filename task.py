import re
# Task time :-

# Input :-

mywords = """
We have example of email address finder
abdealidodia@gmail.com
abdeali@gmail.com
xyz.com
ABDEALi@gmail.com
ABd@yahoo.com
"""
# You need to find out correct email address from your string
pattern = r'[a-zA-Z0-9]{2,}\@[a-zA-Z]{2,}\.[a-zA-Z]{2,}'
final_value = (re.findall(pattern, mywords))
print(final_value)
'''
for i in final_value:
    print(i)
'''