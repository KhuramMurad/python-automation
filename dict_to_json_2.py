import json

os_dict = [{'Name': 'CentOS', 'Version': '7', 'Install': 'yum', 'Owner': 'Redhat', 'Kernel': '3.10'}, {'Name': 'Ubuntu', 'Version': '17.10', 'Install': 'apt', 'Owner': 'Canonical', 'Kernel': '4.13'}]
print(os_dict)
fileNameToBeSaved="os_info"
with open(fileNameToBeSaved, 'w') as Json_File:
    json.dump(os_dict, Json_File, indent=3)