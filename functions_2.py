'''
def myfunc(*data): # add "*" before parameter and pass the arguments without defining one by one
    print(f"my server is {data[0]} my ip is {data[1]} and my os is {data[2]}")



mylist = ["Google", "192.168.1.1", "CentOS-9"]
#myfunc("Google", "192.168.1.1", "CentOS-9")
myfunc(*mylist) # same can be done through a list

def myfunc(*mydata):
    for i in mydata:
        #print(type(i))
        print(i)
        #return None

myfunc(4,6,9)

# **args

def mydict_func(**mydata): # here value can be passed through "**mydict" but in this case dictionary name has to be mentioned in for loop as "mydict.items"
    for key,value in mydata.items():
        print(key,value)


mydict = {'Server':"Google", 'IP': '192.168.8.1', 'OS' : 'Windows 11'}
mydict_func(**mydict)
################################3
# lamda function

#before

def funct(num1, num2):
    sum = num1+num2
    return sum
print(funct(12,45))
'''
# now with lambda
'''
syntax:-
function_name = lambda <"variables" as parameters>:<expression>
print(<function_name>(<arguements> for example <agrument1>, argument2>))

sum = lambda num1,num2:num1+num2
print(sum(12,45))

sum = lambda num1, num2 : num1 if (num1 >= num2) else num2
print(sum(2,4))

# sort data in a tuple with lambds

my_tuple = ((2,3), (4,6), (7,3))
sorted_data = sorted(my_tuple, key=lambda tuple_values: tuple_values[1]) # "key" is part of sorted method
print(sorted_data)

 # filtering a list to filter odd or even number

my_list = [1,2,4,5,6,8,9,11]
odd_nums = list(filter(lambda numbers: numbers%2 != 0 , my_list))
even_nums = list(filter(lambda numbers: numbers%2 == 0 , my_list))
print("Odd numbers", odd_nums)
print("Even Numbers", even_nums)

'''
import os
def myfunc():
    print("This a simple function call")
'''
# method 1
def main():
    print(os.listdir(os.getcwd()))

if (__name__=="__main__"):
    main()
'''
# method 2

if (__name__=="__main__"):
    print(os.listdir(os.getcwd()))
    print(os.system("dir"))
    print("this is main function call")