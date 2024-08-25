immutable_var=(1,5,'cod',0.1)
print(type(immutable_var))
#immutable_var[0]=7 данные не изменяются, так как в кортеже не возможно изменять данные это заложенно в структуру
print(immutable_var)
mutable_list= [1,2,'a','b']
print(mutable_list)
mutable_list[3]='Modified'
print(mutable_list)
