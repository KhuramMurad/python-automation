import paramiko

# Define SSH connection parameters
hostname = "192.168.56.101"
username = "root"
password = "1234"

# Create an SSH client instance
client_linux = paramiko.SSHClient()
client_linux.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the remote Linux server
client_linux.connect(hostname=hostname, username=username, password=password)

# Define the commands to retrieve memory information
total_mem_cmd = "free -g | grep Mem | awk '{print $2}'"
used_mem_cmd = "free -g | grep Mem | awk '{print $3}'"
available_mem_cmd = "free -g | grep Mem | awk '{print $7}'"

# Execute the commands on the remote server
stdin, stdout, stderr = client_linux.exec_command(total_mem_cmd)
total_mem = stdout.read().decode().strip()

stdin, stdout, stderr = client_linux.exec_command(used_mem_cmd)
used_mem = stdout.read().decode().strip()

stdin, stdout, stderr = client_linux.exec_command(available_mem_cmd)
available_mem = stdout.read().decode().strip()

# Close the SSH connection
client_linux.close()

# Print the results
print("Total Memory: {} GB".format(total_mem))
print("Used Memory: {} GB".format(used_mem))
print("Available Memory: {} GB".format(available_mem))
