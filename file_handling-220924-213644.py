with open('C:\\Users\\AbdealiDodiya\\Desktop\\DevOps\\Python\\Lecture 33\\abd.txt') as file:
    data=file.readlines()
    #print(data)
    for i in data:
        word=i.split()
        print(word)
