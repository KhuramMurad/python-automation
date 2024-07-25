import csv

# Input CSV file path
input_data = r"D:\OneDrive\Al Nafi Emerging Technologies Study Material\DevOps Track Level 4\3- Python Automation\Lecture 38\servershealth-220930-214947.csv"
# List to store filtered data
newlist = []

# Read input CSV file
with open(input_data, newline='') as csv_file:
    csv_data = csv.reader(csv_file)
    header = next(csv_data)  # Read and store the header row
    for row in csv_data:
        if row[2] == "RHEL":
            newlist.append(row)

# Output CSV file path
output_csv = 'new_csv.csv'

# Write filtered data to a new CSV file
with open(output_csv, 'w', newline='') as newcsv:
    new_data = csv.writer(newcsv)
    new_data.writerow(header)  # Write the header row to the new file
    new_data.writerows(newlist)  # Write the filtered data rows

print(f"Filtered data has been added to the new file: {output_csv}")

# Print the header row
print(",".join(header))
# Print the filtered data
for row in newlist:
    print(",".join(row))
