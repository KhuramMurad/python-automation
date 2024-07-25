#string slicing


var1='Khuram'
print("The provided string is :", var1)
#slicing
# K h u r a m
# 0 1 2 3 4 5 --> Positive Index Values
#  K  h  u  r  a  m
# -6 -5 -4 -3 -2 -1 --> Negative Index Values

print(var1[0])
print(var1[0:5]) #--> "5" means values will be sliced from 0 to 4
print(var1[2:5])  # out put "ura"
#-
print(var1[-6:-1]) #Khura
print(var1[-6:2]) #Kh
print(var1[-5:4]) #hur

#index value

value='Khurram'
print(value.index('r',3 ))


