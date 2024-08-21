#index start from zero also whitespace counted as index
# 0 1 2 3 4 5 6 7 8 9 10 .....

#     [0:0] [-2:-1] = range index and [0] or [-1] or [ 5] single index
name_variable = "Amar Dagaura"
index_variable = "0123456789"

print(name_variable[:])
print(name_variable[0])
print(name_variable[0:7]) # it will print 0 to 6 indexe by excluding last 7th index or character

print(name_variable[:-1]) # excluding the last character by -1

print(name_variable[-1]) # printing the last character

print(name_variable[-7]) # it will print 7th character

print(name_variable[-1]) # it will print)

#print(index_variable[0:-1])

print(index_variable[-5:-1]) 

