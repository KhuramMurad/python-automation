import json

myinfo = {
	"server1" : {
		"IBM": {
			"datacenter":"Bangalore",
			"env": {
				"PR": "192.168.1.1",
				"DR": "192.168.1.2"
				}
			}
		    }
	}
print(type(myinfo))

mypath="user_details.json"
with open(mypath,'w') as df:
    json.dump(myinfo,df,indent=4)