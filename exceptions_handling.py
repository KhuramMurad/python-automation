# exception handling
'''
try:
    a=100
    print("the value of a is : ", a)
    print("the value of b is : ", b)
except:
    print('something is wrong with your code')

# more proper way to handle this error
try:
    a=100
    print("the value of a is : ", a)
    print("the value of b is : ", b)
except Exception as e: # "e" is recommended
    print('something is wrong with your code', e)

# index error

 print(my_list[6])
          ~~~~~~~^^^
IndexError: list index out of range

try:
    my_list = [2, 3, 5, 6, 8, 9]
    print(my_list[6])
except Exception as e:
    print("Warning !!!", e)
'''

# import error
try:
    import ossss
    print(os.listdir())
except Exception as e:
    print("Warning !!!", e)

