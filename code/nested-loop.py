# for x in range(5):
#     for y in range(3):
#         print(f"({x},{y})")

# for x in "python":
#     print(x)

# for x in [1,2,3,4]:  #list
#     print(x)

# number = 100
# while number > 0:
#     print(number)
#     # number //=  2
#     number =  number // 2


command = ""
while command.lower() != "quit":
    command = input(">")
    print("Here is your", command)