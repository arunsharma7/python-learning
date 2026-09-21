#Print count of words in a string

a= "I am going to the market and I am going to buy some fruits and vegetables"
def count_words(a):
    words = a.split()
    print(words)
print(count_words(a))