import re

my_words = "Hi, I am Khuram Murad from Pakistan, We are learning Python in DevOps course. We are also learning Python 2 & Python 3 and DevOps related tools. We have a comprehansive course by Al-Nafi to learn DevOps and emerging tecnologies"
#patters = "We"
#pattern = "Python[23]"
pattern = "Python ['', 23]"
print(re.findall(pattern, my_words))

