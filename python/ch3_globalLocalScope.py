# def spam():
#     eggs=31337
#     return eggs
# spam()
# print(spam())

# def spam():
#     eggs = 99
# 	#bacon()
# 	print(eggs)

# def bacon():
#     ham=101
#     eggs=0

# spam()
# def spam():
#     print(eggs)
# eggs=42
# spam
# print(eggs)

def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print("Error: Invalid argument.")

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))