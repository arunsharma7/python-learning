#Write a python program to remove duplicates , keep the first occurrance 

#a= [1, 2, 3, 4, 5, 1, 2, 3, 6, 7]
def remove_duplicates(a):
    for i in a:
        while a.count(i) > 1:
            a.remove(i)
    return a
print(remove_duplicates([1, 2, 3, 4, 5, 1, 2, 3, 6, 7]))



a = [1, 2, 3, 2, 4, 1, 5, 3]
def remove_duplicates1(a):
    result = []
    for i in a:
        if i not in result:
            result.append(i)
    return result
print(remove_duplicates1(a))