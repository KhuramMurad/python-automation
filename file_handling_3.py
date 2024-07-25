# reading JSON files
import json
file = r"D:\OneDrive\Al Nafi Emerging Technologies Study Material\DevOps Track Level 4\3- Python Automation\Lecture 35\my-220924-215334.json"
with open(file , 'r') as json_file:
    my_dictionary = json.load(json_file)
    print(my_dictionary)
    print("Keys are ")
for key in my_dictionary: # we only need keys here
        print(key)
password_apache = (my_dictionary['password_apache'])
#print(password_apache)

print("\nMy Apache Username is 'Rumman' and my password is : ", password_apache)


