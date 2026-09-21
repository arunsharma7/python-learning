#write to a file
f = open("JohnDoe.txt", "a")

string = '''
Adding more data about John Doe
I am not sure what I am going to add for this program you know.
'''

f.write(string)

f.close()