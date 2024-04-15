my_string = "giraffe"

# g i r a f f e
# 0 1 2 3 4 5 6
# g  i  r  a  f  f  e
#-7 -6 -5 -4 -3 -2 -1

# Printing first element of the string using + and - indices
# It wil print g
print(my_string[0])
print(my_string[-7])

# Printing last element of the string using + and - indices
# It will print e
print(my_string[6])
print(my_string[-1])

# Printing first 3 elements of the string using + and - indices
# It will print gir
print(my_string[0:3])
print(my_string[-7:-4])

# Printing last 3 elements of the string using + and - indices (For negative indices to print lats 3 elements you have to start from -3 and leave the end colum blank. If you put -1 in last column it will only print 2 elements (like ff) )
# It will print ffe
print(my_string[4:7])
print(my_string[-3:])
# It will print ff
print(my_string[-3:-1])
