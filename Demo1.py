# #print("Shashwat Malasi")
# #test = 21
# #print("The value is = {}".format(test))
#
# #print(type(test))
#
# testList = [2, 1.5, "shashwat", 'Malasi']
#
# testList[2] = "Shashwat"
#
# #print(testList)
#
# testList.append("Uttarakhand")
#
# print(type(testList[4]))
#
# del testList[1]
#
# print(testList)
# print(len(testList))
#
#
#
# tup = (2, 3, 4, 5, 5, "Shashwat")
#
# print(tup[3])
# print(tup)
#
#
# dict = {1: "Shashwat", 2: 3.5, "3": "Malasi"}
#
# print(dict)
#
# print(dict['3'])
#
#
# dict["firstName"] = "Kumud"
# dict["lastName"] = "Malasi"
#
# print(dict['firstName'])
#
# #Sum of the first 5 Natural Numbers i.e 1+2+3+4+5
# sum=0
# for i in range(1,6):
#     sum = sum + i
# print(sum)
#
#
#
#
# summation = 0
# for j in range(1, 10, 2):
#     summation = summation + j
# print("The sum of the first 5   odd natural numbers is = {}".format(summation))

# it = 10
# while it > 1:
#     if it == 9: # At this spot, all the executions below this line will be surpassed by the interpreter. Hence, we're stuck in the infinite loop
#         continue
#     if it == 3:
#         break
#     print(it)
#     it = it -1


#
# it = 10
# while it > 1:
#     if it == 9: # At this spot, all the executions below this line will be surpassed by the interpreter. Hence, we're stuck in the infinite loop
#         it = it - 1
#         continue
#     if it == 3:
#         break
#     print(it)
#     it = it -1

#------------FUNCTIONS----------------------------------
def testFunc():
    print("Welcome to this function")

#testFunc()

#------------CLASSES & OOPS------------------------------
class Calculator:
    num = 100 #class variable
    #default constructor

    def __init__(self, a, b):
        self.firstNum = a #Catching the actual parameters into the formal parameters
        self.secondNum = b
        num2 = 101 #Instance variable- Inside the constructor
      #  print("As soon as the object is created, the default constructor is automatically run!!!")
       # print("The value of the instance variable is = {}".format(num2))
       # print("The values of the passed variables are = {}, {}".format(a, b))
    def getData(self):
        print("Inside the getData function!")

    def summation(self):
        return self.firstNum + self.secondNum + Calculator.num

obj = Calculator(2,3)
# obj.num

print("The sum is = {}".format(obj.summation()))
