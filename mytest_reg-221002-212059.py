
import re
myword="Abdeali Dodiya from bangalore , We are learning python and in this course we will learn two version such python2 and python3, We will learn Python selenium in this course"
pattern="python2|python3|python|Python"
print(re.findall(pattern,myword))
