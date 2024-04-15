'''def reverse(name):
    reverseName = ""
    for i in range(len(name), 0, -1):
        reverseName = reverseName+name[i-1]
    return reverseName


name = input("What is your name? ")
print("Your name reversed is:", reverse(name))
'''
# to reverse iterate the string
myListStr = "sameer"
# :: means it will iterate through each letter but from the end since it is -1
print(myListStr[::-1])
