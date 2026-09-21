#write to a file
f = open("JohnDoe.txt", "w")

string = '''
John 1 doe is always used as a name 
when the person identity is not known or we 
want to hide, here the person is 40 years old and dead
'''

f.write(string)
print(string)
f.close()