def collatz(number):
    if number % 2 == 0:
        return number//2
    elif number % 2 ==1 :
        return 3*number+1

try:
    print("Enter number:")
    input_name = int(input())
    while True:
        input_name=collatz(input_name)
        print(input_name)
        if input_name ==1:
            break

except ValueError:
    print("Input format if incorrect, please enter an integer!")

