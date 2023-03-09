######################
# Test 1
######################
# import m3
# print(m3.m3_print3())

######################
# Test 2 (不能執行. 因為m3.py在資料夾my_pkg裡面.)
######################
# from my_pkg import m3 
# print(m3.m3_print3())

######################
# Test 3
######################
# from m3 import *
# print(m3_print3())

######################
# Test 4
######################
from m3 import m3_print1, m3_print2, m3_print3
print(m3_print3())


