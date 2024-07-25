import json
file = r"D:\OneDrive\Al Nafi Emerging Technologies Study Material\DevOps Track Level 4\3- Python Automation\Lecture 35\os-220924-215341.json"
with open (file, 'r') as jf:
    my_dict = json.load(jf)
    print(my_dict)
    #print(type(my_dict))
    for i in my_dict:
        #print(i)
        for key, value in i.items():
            if value == 'Ubuntu':
                print(f"my Ubuntu version is : ", i['Version'])
            elif value == 'CentOS':
                print(f"my CentOS version is : ", i['Version'])
