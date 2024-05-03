# items = 0
#
# # if items != 2:
# #     raise Exception("The quantity is 0")
#
# if items != 2:
#     pass
#
# #assert(items == 2)
# assert items == 0, "The number of items must be positive non-zero"

items = 2

assert items > 0, "The value is below 1"

try:
    with open("testlog.txt", 'r') as reader:
        reader.read()
except:
    print("Cannot locate the file!")