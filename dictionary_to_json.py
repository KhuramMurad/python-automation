import json

myinfo = {
    "server1": {
            "IBM": {
                "datacenter": "Bangalore",
                "env": {
                        "PR": "192.168.1.1",
                        "DR": "192.168.1.2"
                }
            }
    }
}
print(myinfo)
mydata = "user_info.json"
with open(mydata, 'w') as json_file:
    #json.dump(myinfo, json_file)
    json.dump(myinfo,json_file, indent=2)
