'''

import os

try:
    os_name = os.popen("cat /etc/os-release | grep -iw \"NAME\" | awk -F = '{print $2}' | tr -d '\"'").read().strip('\n')
    if os_name == 'Ubuntu' or os_name == 'redhat':
        print(f"my OS is : {os_name}")
        df_cmd = os.popen("df -h  | grep -v 'tmpfs' | grep -v 'snapfuse' | grep -v 'none' |awk 'NR!=1' | awk '{print $1,$2,$3,$4,$5,$6}' | sed -e 's/%//g' | sed -E \"s/ +/,/g\" | sed \"s/$/,$(date '+%F %T')/g\" | sed \"s/$/,$(hostname -I | awk '{print $1}')/g\" |  sed \"s/$/,$(hostname)/g\" > mycsvfile.csv").read()
        print(df_cmd)
    else:
        print("Other os found", os_name)
except Exception as e:
    print("Something having issue", e)
'''
import os
import json

try:
    myjson_file = "linux.json"
    with open(myjson_file, 'r') as file:
        dict_data = json.load(file)

    os_flavour = dict_data.get('os_flavour')
    df_cmd = dict_data.get('df_cmd')

    if os_flavour:
        os_name = os.popen(os_flavour).read().strip()
        if os_name in ['Ubuntu', 'redhat']:
            print(f"My OS is: {os_name}")
            if df_cmd:
                df_output = os.popen(df_cmd).read()
                print(df_output)
                print("CSV file generated successfully in the current directory")
            else:
                print("No 'df_cmd' specified in the JSON file.")
        else:
            print(f"Other OS found: {os_name}")
    else:
        print("No 'os_flavour' specified in the JSON file.")

except Exception as e:
    print("Something went wrong:", str(e))
