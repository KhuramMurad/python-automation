import re
myword="""
We have example of email address finder 
abdealidodia@gmail.com
abdeali@gmail.com
xyz.com
ABDEALi@gmail.com
ABd@yahoo.com
"""

pattern=r"[a-zA-Z0-9-\.]{2,}\@[a-zA-Z]{2,}\.[a-zA-Z]{2,}"
print(re.findall(pattern,myword))