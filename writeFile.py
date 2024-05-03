#Manually closing the file after opening it
# file = open("test.txt")
# file.close()

#Single line opening
with open('test.txt', 'r') as readerFile:
    content = readerFile.readlines()
    #for i in reversed(content):
     #   print(i)
    reversed(content)
    with open('test.txt', 'w') as writerFile:
        for i in reversed(content):
            writerFile.write(i)


