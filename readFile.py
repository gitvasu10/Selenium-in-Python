file = open('test.txt')
#---------------------------------------------------Reading all the contents of the file--------------------------------------------

#file.read() #This line will read the contents but won't print them since it is only in the reading mode not the printing one.
#fileRead = file.read()
#print(file.read()) #normal print

#Read n number of characters by passing the parameters
#print(fileRead[:1])

#print(file.readline())
#print(file.readline(2)) -----> Will still print the first 2 characters only


# lineRead = file.readline()
# while(lineRead != ""): #Check the empty character(not a whitespace!)
#     print(lineRead)
#     lineRead = file.readline()
# file.close()

#CONVERTING THE FILE INTO A LIST

lines = file.readlines()
#print(lines)

for i in lines:
    print(i*2)

