#############################################################################
# shadow copy
#############################################################################
# a = [1,2,3]
# b = a
# a_list = list(a)
# a_index = a[:]
# a_copy = a.copy()
# a.append(5)
# print("Shallow copy")
# print(f"a = {a}, id(a) = {id(a)}")
# print(f"b = {b}, id(b) = {id(b)}")
# print(f"a_list:{a_list}, id(a_list)={id(a_list)}")
# print(f"a_index:{a_index}, id(a_index)={id(a_index)}")
# print(f"a_copy:{a_copy}, id(a_list)={id(a_copy)}")

#############################################################################
# Argument passing (empty + positional/ketword argument)
#############################################################################
# def addition(x = 0, y = 0):
#     return x-y

# print(addition())
# print(addition(10))
# print(addition(20, 10))
# print(addition(x = 20, y = 10))
# print(addition(y = 10, x = 20))

################################################################
# pass by sharing - Use mutable data type
#############################################################################
# def foo_list(lst):
#     print(id(lst))
#     lst.append(1)
#     print(id(lst))
#     lst = [2]
#     print(lst, id(lst))
    
# m = []
# print(id(m))
# foo_list(m)
# print(id(m))
# print(m)

#############################################################################
# pass by sharing (#immutable data type)
#############################################################################
# def foo_int(val):
#     print(id(val))
#     num = val
#     print(id(num))
#     val = 10
#     print(val, id(val))
    
# v = 5
# print(id(v))
# foo_int(v)
# print(id(v))
# print(v)

#############################################################################
# Global/local variables (#immutable argument)
#############################################################################
# a = 5

# def modification(num):
# 	#global a

# 	print("[Local In] num = {}, id(num) = {}".format(num, id(num)))
# 	a = num
# 	print("[Local Out] a = {}, id(a) = {}".format(a, id(a)))

# print("[Global In] a = {}, id(a) = {}".format(a, id(a)))
# modification(20)
# print("[Global Out] a = {}, id(a) = {}".format(a, id(a)))

#############################################################################
# Global/local variables (#mutable argument)
#############################################################################
# list_1 = [1,2,3,4]

# def modification(lst):
# 	#global list_1

# 	print("[Local In] lst = {}, id(lst) = {}".format(lst, id(lst)))
# 	list_1 = lst
# 	print("[Local Out] list_1 = {}, id(list_1) = {}".format(list_1, id(list_1)))

# print("[Global In] list_1 = {}, id(list_1) = {}".format(list_1, id(list_1)))
# modification([5,6,7,8])
# print("[Global Out] list_1 = {}, id(list_1) = {}".format(list_1, id(list_1)))

#############################################################################
# *args 
#############################################################################
# def sum_1(x , y):
#     return x + y

# def sum_2(*args):
#     print(args)
#     print(type(args))
#     results = 0
#     for num in range(0, len(args)):
#         results += args[num]
#     return results

# print(sum_1(1,2))
# print(sum_2(1,2,3,4,5))

#############################################################################
# ***kwargs
#############################################################################

# def func(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     print(kwargs['name'])
#     print(kwargs['age'])
    
# func(name="Gion", age=20)
