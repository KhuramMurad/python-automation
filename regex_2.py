import re
mytext = "This is demo text to be used to check regular expressions\n pattern matchin gin Python 2 and Python 3.\n This is Python Automation Lecture 21"
#pattern = "\w\w\w\w\w\w"
#pattern = "\W" # finds spaces and special characters
#pattern = "21$"
pattern = r"\n"
print(mytext)
print(re.findall(pattern, mytext))
#print(dir(re))