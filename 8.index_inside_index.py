var = "_hello_world_!"

#print(var[0])
#print(var[6])
#print(var[12])
#print(var[13])

another_var = var [1:6] + var[7:12] + var [13]
print(another_var)

_var = var [1:6]
var_ = var [7:12]
_var_ = var [13]
print(_var + var_ + _var_)