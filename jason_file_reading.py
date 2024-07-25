import json

myfile = r"D:\OneDrive\Al Nafi Emerging Technologies Study Material\DevOps Track Level 4\3- Python Automation\Lecture 35\my-220924-215334.json"
with open (myfile , 'r') as json_file:
    dictionary_data = json.load(json_file)
    print(dictionary_data)
    print("Keys are")
    for key,value in dictionary_data.items():
        print(key, value)

password_ansible = (dictionary_data['password_ansible'])
print("my Ansible Username is 'Khuram and my password is : ", password_ansible)
