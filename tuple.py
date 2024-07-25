tup1= () # empty tuple boolean value is "False"
print(bool(tup1))
#
tup1 = (3,5,7,9) # if tuple has values , its boolean value will be "True".
print(bool(tup1))

#nested tuple

tup2 = ("KMS", [2,4,7,[99, 88, 77 ]], (2,7,9,3, (33,22,11)))
print(tup2)
print(tup2[1][3][1])
print(tup2[2][4][1])
#

abd = "abd"
print((abd, )*2)
