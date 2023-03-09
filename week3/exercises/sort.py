############################################################################
#sorted
#############################################################################
# x1 = [4,1,2,3]
# print("origianl data: x1 = ", x1) # [4, 1, 2, 3]
# print("origianl address: x1 = ", id(x1)) # 1856293457984
# y1 = sorted(x1)
# print("sorted() data y1 = ", y1) # [1, 2, 3, 4]
# print("sorted() address of y1 = ", id(y1)) # 1856293458368
# print("address of x1 = ", id(x1)) # 1856293457984


#############################################################################
#built-in method: sort
#############################################################################
# x2 = [4,1,2,3]
# print("origianl data: x2 = ", x2) # [4, 1, 2, 3]
# print("origianl address: x2 = ", id(x2)) # 2321626845632
# y2 = x2.sort() # y2 = None
# print ("x2.sort() data: x2 = ", x2) # [1, 2, 3, 4]
# print ("x2.sort() address: x2 = ", id(x2)) # 2321626845632
# print("y2 = x2.sort(), return value of y2 = ", y2) # None
# print("y2 = x2.sort(), return address of y2 = ", id(y2)) # 140726574062808 (address of None)