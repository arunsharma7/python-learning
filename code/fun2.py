# def increment(number, by=1):
#     print()
#     return number + by

# # result = increment(2,1)
# # print(increment(number=2,by=1))
# print(increment(2,5))

#collection of arguments

def multiply(*numbers):
    total = 1
    for number in numbers:
        #total *= number
        total = number*total
    return total

print(multiply(2,3,4,5))