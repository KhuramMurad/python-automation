# zero division error
'''
try:
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter a number"))

    division = num1/num2
    print(division)
except Exception as e:
    print("Be careful !!!", e)

# value error
try:
    num1 = int(input("Enter a number "))
    num2 = int(input("Enter a number "))

    division = num1/num2
    print(division)
except Exception as e:
    print("Be careful !!!", e)
'''
try:
    import os
    x = "ABD"
    y="Ali"
    print("My value is ", x)
    print("My value is ", y)
    mylist = [2, 7, 8, 9]
    print(mylist[3])
    os.system('hostname')
    a = int(input("Enter the number:"))
    b = int(input("Enter the number:"))

    result = a / b
    print(result)
except NameError:
    print("Something having issue in your variable, Please check variable define or not")
except IndexError:
    print("Please check your data structure index value should be within range")
except ModuleNotFoundError:
    print("Please check module name or module available in your machine")
except ZeroDivisionError:
    print("Please check value , Zero you can not devide with any value ")
except ValueError:
    print("Error !!!, please enter the integer value")
# and
except Exception as e:
    print("Something is wrong with your code please check it again")
else:
    print("else statement, program executed without any error")

finally:
    print("this message will display in every situation")

