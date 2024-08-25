immutable_var=(1,5,'cod',0.1)
print(type(immutable_var))
#immutable_var[0]=7 не изменяемые элементы кортежа
print(immutable_var)
mutable_list= [1,2,'a','b']
print(mutable_list)
mutable_list[3]='Modified'
print(mutable_list)
