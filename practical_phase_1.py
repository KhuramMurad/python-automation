'''
Task 1 :-
Please debug below error and print the mentioned variable.
glass_of_water=12.ML
glass_of_water=12.ML
File "<stdin>", line 1
glass_of_water=12.ML
^
SyntaxError: invalid decimal literal
#solution
glass_of_water=12
print(glass_of_water)

#Task 3 :-
#Python Program to Check if a Number is Positive, Negative or 0

number = eval(input("Enter a number : "))
if number > 0:
    print(f"Number {number} is positive")
elif number < 0:
    print(f"Number {number} is Negative")
else:
    print(f"Number is 0 ")


#Task 4 :-
#Python to check character is Vowel or not

character = input("Enter the character : ")
if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
    print(f"The character \"{character}\" is a Vowel")
else:
    print(f"The character \"{character}\" is not a Vowel")

#Task 5
str = 'Abdeali Dodia Bangalore'
print(str.split())
print('-'.join(str))


# Task 6 :-
# Reversing a List in Python

mylist = [1, 2, 3, 4, 5, 6, 7]
mylist.reverse()
print(mylist)

# Task 7 :-
# Trim Whitespace From a String
my_word = " Abdeali "
print(my_word.strip())



#Task 8 :-

# Get the File Name From the File Path.
import os
file = os.path.basename("D:\OneDrive\Al Nafi Emerging Technologies Study Material\DevOps Track Level 4\3- Python Automation\Lecture 23\practical_phase_1.py")


#Task 9 :-
#Get the Full Path of the Current Working Directory.
import os
print(os.getcwd())
#print(os.path.dirname(os.path.abspath("abd.txt")))
#print(os.path.abspath(os.getcwd()))
print(str(os.path.splitext(file)[0]))
'''

# Task 10 :-
# Insert a number to any position in a list
list = [2,3,5,6,8,9]
print(list)
print(len(list))
number = (input("Enter a number : "))
position = int(input("Enter position: "))
#list.index(number,position)
list.insert(position,number)
print(list)
print(len(list))
