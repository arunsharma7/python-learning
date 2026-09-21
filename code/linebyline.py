f = open("arun.txt", "r")

for line in f:
    print(line)

f.close()

'''try:
    content = f.read()

    f.close()

except FileNotFoundError:
    print("No File")
    '''