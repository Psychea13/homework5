immutable_var = 1, 2.5, True, 'Привет!'
print(immutable_var)

#immutable_var[1] = 3.1
#Изменить значения элементов кортежа нельзя, т.к. кортеж относится к неизменяемым типам данных.
#Если попытаться изменить какой-либо элемент, то получится ошибка. Кортеж не поддерживает обращение по элементам.

mutable_list = [1, 2.5, True, 'Привет!']
mutable_list [0] = 7
mutable_list [1] = 5.0
mutable_list [2] = False
mutable_list [3] = 'Пока!'
print(mutable_list)
