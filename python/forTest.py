# q_list=["吳思佩","邱浩偉","猜猜看"]

# for q in q_list:
#     print(q)

# list=[1,2,3,4,5,6,7,8,9]

# for n in list:
#     if n%2==0:
#         break
#     print(n)

# print("迴圈結束")
# import math
# r=5


# def cirArea(r):
#     area=math.pi*(r**2)

#     return area

# print(cirArea(r))

while True:
    print("Who are you?")
    name = input()
    if name!= "Joe":
        continue
    print("Hello "+name+". What is the password(It's a fish)")
    password= input()
    if password == "swordfish":
        break

print("Access Grant!")
