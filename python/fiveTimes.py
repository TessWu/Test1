# print("My name is ")
# for i in range(5):
#     print("Jimmy five times("+str(i)+")")
#     break
# for i in range(5,-1,-1):
#     print(i)
# import random
# for i in range(5):
#     print(random.randint(1,10))
import sys

while True:
    print("Type exit to exit.")
    test=input()
    if test == "exit":
        sys.exit()
    print("You type"+test)