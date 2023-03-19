#############################################################################
# (A) Data Type - int (immutable))
#############################################################################

# (A.1) Operations
# [Descrition] Operations: addition(+)/substration(-)/multiplication(*)/division(/)/mod(%)/exponent operator(**)
# [Sample code]
# print(3+2) # 5
# print(3-2) # 1
# print(3*2) # 6
# print(3/2) # 1.5
# print(int(3/2)) # 1
# print(3%2) # 1
# print(3**2) # 9

# (A.2) Arithmetic operators
# [Descrition] Build-in methods: abs()/pow()/max()/min()/round()
# [Sample code]
# print(abs(1))  # 1
# print(abs(-1)) # 1
# print(pow(2,3)) #8 
# print(max(1,2,3,4,5,6)) # 6
# print(min(1,2,3,4,5,6)) # 1
# print(round(1.5)) # 2 (round up if the rounded up value is even number)
# print(round(2.5)) # 2 (round down if the rounded up value is odd number)

# (A.3) Type casting
# [Descrition] Casting type: int()/float()/str()
# [Sample code]
# print(1.1+1.1) # 2.2
# print(int(1.1)+int(1.1)) # 2
# print(int(2.2)) # 2
# print(float(2)) # 2.0
# print(1+1) # 2
# print(str(1)+str(1)) # 11

# (A.4) Math modules
# [Descrition] Methods: e/pi/floor()/ceil()
# [Sample code]
# import math # required module 'math' needs to be import
# print(math.e) # 2.718281828459045
# print(math.pi) # 3.141592653589793

#############################################################################
# (B) Data Type - float (immutable)
#############################################################################
# (B.1) Basic
# [Descrition] Basic operations
# [Sample code]
# float_1 = 1.23
# string_1 = str(float_1)
# print(float_1) # 1.23
# print(type(float_1)) # <class 'float'>
# print(string_1) # typecasting to string 1.23
# print(type(string_1)) # <class 'str'>

# #############################################################################
# (C) Data Type - str (immutable)
#############################################################################

# (C.1) String Indexing (normal indexing)
# [Descrition] String indexing starts from 0. (Direction positive)
# [Sample code]
# name = "Python"
# print(name) # Python
# print(f"index 0: {name[0]}") # 'P'
# print(f"index 1: {name[1]}") # 'y'
# print(f"index 2: {name[2]}") # 't'
# print(f"index 3: {name[3]}") # 'h'
# print(f"index 4: {name[4]}") # 'o'
# print(f"index 5: {name[5]}") # 'n'
# #print(f"index 6: {name[6]}") #  Error. Index out of range.

# (C.2) String Indexing (negtive indexing)
# [Descrition] String indexing starts from 0. (Direction negtive)
# [Sample code]
# name = "Python"
# print(name) # Python
# print(f"index 0: {name[0]}") # 'P'
# print(f"index -1: {name[-1]}") # 'n'
# print(f"index -2: {name[-2]}") # 'o'
# print(f"index -3: {name[-3]}") # 'h'
# print(f"index -4: {name[-4]}") # 't'
# print(f"index -5: {name[-5]}") # 'y'
# #print(f"index -6: {name[-6]}") # 'P'
# #print(f"index -7: {name[-7]}") # Error. Index out of range.

# (C.3) Immutable Demostration
# [Descrition] String value CANNOT be changed.
# [Sample code]
# name = "Python"
# print(name[0]) # 'P'
# name[0] = 'p'  # TypeError: 'str' object does not support item assignment
# print(name[0]) 

# (C.4) String Slicing
# [Descrition] format: [start_index(include): end_index(not include): step_size]
# [Sample code]
# name = "Python"
# print(name[1:3]) # yt
# print(name[1:4:2]) # yh
# print(name[-4:-1:1]) # tho
# print(name[-4:-1:-1]) # (blank)
# print(name[2:5:1]) # tho
# print(name[2:5:-1]) # (blank)
# print(name[-1:0]) # (blank)
# print(name[-1:0:-1]) # nohty
# print(name[0:-1]) #  Pytho
# print(name) # Python
# print(name[::]) # Python
# print(name[::1]) # Python
# print(name[::-1]) # nohtyP (reverse string)    

# (C.5) Concatenate Strings
# [Descrition] Combine two strings by using '+'
# [Sample code]
# string_1 = "Hello"
# string_2 = "Python"
# print(string_1 + string_2) # HelloPython
# print(string_1 + " " + string_2) # Hello Python

# (C.6) Format Strings
# [Descrition] Combine string and int by using format.
# [Sample code]
# string_1 = "Hello Python. I am No {}"
# num = 10
# print(string_1.format(num)) # Hello Python. I am No 10

# (C.7) Escape Characters
# [Descrition] An Escape character is a backslash '\' followed by the character that you want to insert.
# [Sample code]
# string_1 = "Hello \"Python\""
# string_2 = "Hello 'Python'"
# string_3 = 'Hello "Python"'
# print("string_1={}".format(string_1)) # Hello "Python"
# print("string_2={}".format(string_2)) # Hello 'Python'
# print("string_3={}".format(string_3)) # Hello "Python"

# (C.8) String Methods
# [Descrition] Other built-in methods for string.
# Note : (*)Those methods do NOT change the original string, but return new values. 
# [Sample code]
# Please ref. w3cschool for string methods.
# string_1 = "Python"
# new_string = string_1.replace("P", "G")
# print(f"original_strng is {string_1} with object address {id(string_1)}")
# print(f"new_string is {new_string} with object address {id(new_string)}")

# (C.9) String typecasting with type list
# [Descrition] typecasting for a string with character by character.
# [Sample code]
# string_1 = "Python"
# new_list = list(string_1)
# print(f"new_list is {new_list}")

#############################################################################
# (D) Data Type - bool (immutable)
#############################################################################

# (D.1) Basic (int)
# [Descrition] It represents one of the two values "True" and "False"
# [Sample code]
# print(2 > 1) # True
# print(1 > 2) # False
# if 2 > 1:
#     print("2 is greater than 1.")
# else:
#     print("2 is smaller or equal than 1.")

# (D.2) Basic (string)
# [Descrition] It represents one of the two values "True" and "False"
# [Sample code]
# string_1 = "Python"
# if string_1:
#     print(f"string_1: {string_1} --> Not empty --> True.")
# if bool(string_1):
#     print("bool(string_1) --> True.")

# (D.3) Basic (list)
# [Descrition] It represents one of the two values "True" and "False"
# [Sample code]
# list_1 = [1,2,3]
# if list_1:
#     print(f"list_1: {list_1} --> Not empty --> {bool(list_1)}.")
# if bool(list_1):
#     print(f"bool(list_1) --> {bool(list_1)}.")

# (D.4) Basic (Empty cases)
# [Descrition]
# a. Any string is True, except empty strings.
# b. Any number is True, except 0.
# c. Any list, tuple, set, and dictionary are True, except empty ones. 
# [Sample code]
# string_1 ="" # string empty
# value_1 = None # value empty
# int_1 = 0 # 0: bool false, others(1,2,3...): bool true 
# list_1 = [] # list empty
# dict_1 = {} # dict empty
# set_1 = set() # set empty
# tuple_1 = () # tuple empty
# print(bool(string_1)) # False
# print(bool(value_1)) # False
# print(bool(int_1)) # False
# print(bool(list_1)) # False
# print(bool(dict_1)) # False
# print(bool(set_1)) # False
# print(bool(tuple_1)) # False
    
#############################################################################
# (E) Data Type - dict (mutable) (unordered)
# ex: {"1":"Red", "2":"Blue", "3":"Green"}
#############################################################################

# (E.1) Basic 
# [Descrition] Basic usage of dict
# [Sample code]
# person = {"name":"Gino", "age":"20"}
# print(person['name']) # Gino
# print(person['age']) # 20
# print(type(person)) # show 'dict'

# (E.2) Mutable 
# [Descrition] Show mutable operation for list
# [Sample code]
# person = {"name":"Gino", "age":"20"}
# print(f"original memory = {id(person)}")
# person['name'] = "Jerry" # mutable (changed the value in original memory address)
# print(f"modified memory = {id(person)}")
# print(person['name']) # Jerry

# (E.3) Unordered 
# [Descrition] Demostration for the unordered case
# [Sample code]
# dict_1 = {"1":"Ted", "2":"Timmy"}
# dict_2 = {"2":"Timmy", "1":"Ted"}
# if dict_1 is dict_2:
# 	print(f"dict_1={id(dict_1)} and dict_2={id(dict_2)} pointed the same memory address.")
# else:
#     print("dict_1 and dict_2 did NOT point to the same memory address.{}, {}". format(id(dict_1), id(dict_2)))
# if dict_1 == dict_2:
# 	print(f"dict_1={dict_1} and dict_2={dict_2} had the same values.")

# (E.4) Built-in methods
# [Descrition] A set of built-in methods provided by Python
# [Note] Refer as https://www.w3schools.com/python/python_ref_dictionary.asp

#############################################################################
# (F) Data Type - list (mutable) (ordered)
#############################################################################

# (F.1) Basic 
# [Descrition] Basic usage of list
# [Sample code]
# friend_1 = "Kevin"
# friend_2 = "Terry"
# friend_3 = "Kerry"
# print(f"{friend_1}, {friend_2}, {friend_3}")
# friend_list = ["Kevin", "Terry", "Kerry"]
# print(f"{friend_list[0]}, {friend_list[1]}, {friend_list[2]}")
# friend_list.append("Gino") # Added a new name 'Gion' into friend_list
# print(friend_list)

# (F.2) Indexing (******) - Position for normal order 
# [Descrition] Basic indexing of list. (Same concept as string)
# [Sample code]
# name = ["P","y","t","h","o","n"] # index from 0,1,2,3,4,5 (normal order) 
# print(name) # ['P', 'y', 't', 'h', 'o', 'n']
# print(f"index 0: {name[0]}") # 'P'
# print(f"index 1: {name[1]}") # 'y'
# print(f"index 2: {name[2]}") # 't'
# print(f"index 3: {name[3]}") # 'h'
# print(f"index 4: {name[4]}") # 'o'
# print(f"index 5: {name[5]}") # 'n'
# #print(f"index 6: {name[6]}") #  Error. Index out of range.

# (F.3) Indexing (******) - Position for negtive order 
# [Descrition] Basic indexing of list. (Same concept as string)
# [Sample code]
# name = ["P","y","t","h","o","n"] # index from 0,-1,-2,-3,-4,-5 (negtive order) 
# print(name) # ['P', 'y', 't', 'h', 'o', 'n']
# print(f"index 0: {name[0]}") # 'P'
# print(f"index -1: {name[-1]}") # 'n'
# print(f"index -2: {name[-2]}") # 'o'
# print(f"index -3: {name[-3]}") # 'h'
# print(f"index -4: {name[-4]}") # 't'
# print(f"index -5: {name[-5]}") # 'y'
# print(f"index -6: {name[-6]}") #  'P'. Same as name[0]
# #print(f"index -7: {name[-7]}") #  Error. Index out of range.

# (F.4) Slicing (******) 
# [Descrition] Basic slicing of list. (Same concept as string slicing)
# [Notes] https://stackoverflow.com/questions/509211/understanding-slicing
# [Rules] 
#    Format : [start_index(include): end_index(not include): step_size] 
#           
#    a. if step_size is positive(正) value:
#       end_index should be greater than(大於) start_index, otherwise empty list(or string). 
#    b. if step size is negtive (負) value 
#       end_index should be lesser than(小於) start_index, otherwise empty list(or string)
#    
#                   +---+---+---+---+---+---+
#                   | P | y | t | h | o | n |
#                   +---+---+---+---+---+---+
#   Slice position: 0   1   2   3   4   5   6
#                  -6  -5  -4  -3  -2  -1
#   Index position:   0   1   2   3   4   5
#                    -6  -5  -4  -3  -2  -1

# [Sample code]
# name = ['P', 'y', 't', 'h', 'o', 'n']
# print(name) # ['P', 'y', 't', 'h', 'o', 'n']
# print(name[1:5]) # ['y', 't', 'h', 'o']
# print(name[0:-1:]) # ['P', 'y', 't', 'h', 'o']
# print(name[0:-1:-1]) # [] ???
# print(name[::-1]) # ['n', 'o', 'h', 't', 'y', 'P']
# print(name[:]) # ['P', 'y', 't', 'h', 'o', 'n']
# print(name[0:-6:-1])

# (F.5) Built-in methods 
# [Descrition] A set of built-in methods provided by Python
# [Note] Refer as https://www.w3schools.com/python/python_ref_list.asp

#############################################################################
# (I) Data Type - tup (immutable) (ordered) = immutable list
#############################################################################
# (I.I) Basic operations 
# [Descrition] The operations are similiar to list (including indexing/slicing rules and methods..)
# [Sample code]
# tup_1 = (5, "20", "Gino")
# print(type(tup_1))
# print(tup_1) # (5, '20', 'Gino')
# print(tup_1[0]) # 5
# print(tup_1[0:2]) # (5, '20')

# (I.2) Immutable
# [Descrition] Immutable demostration
# [Source code]
# tup_1 = (5, "10", "Gino")
# tup_1[0] = 20 # TypeError becuase tuple is immutable.(cannot assign)
# print(tup_1)

# (I.3) Tuple packing.(*****)
# [Descrition] Common used in ML and AI.
# [Source code]
# tup_pack_1 = 1, 2, 3, 4, 5 # tuple packing
# print(tup_pack_1)
# print(type(tup_pack_1))

# (I.4) Tuple unpacking.(*****)
# [Descrition] Common used in ML and AI.
# [Source code]
# height, weight = (180, 80) # tuple unpacking
# print(height)
# print(weight)

# (I.5) Tuple packing + tuple unpacking (***)
# [Descrition] A skill to exchange two variables
# [Source code]
# value_1 = 10
# value_2 = 20
# value_1, value_2 = value_2, value_1 # tuple packing + tuple unpacking(*)
# print(value_1)
# print(value_2)

# (I.6) Basic methods
# [Descrition] A set of methods that used for tuple.
# [Note] Refer as https://www.w3schools.com/python/python_ref_tuple.asp

#############################################################################
# (J) Data Type - set (unordered)
#############################################################################
# (J.I) Basic
# [Descrition]  Basic
# [Sample code]
# set_1 = set() # init a new set
# set_2 = set({1,2,3,4,5}) # add init values in set
# print(set_1) # set()
# print(set_2) # {1, 2, 3, 4, 5}

# (J.2) Basic
# [Descrition]  change data type 'list --> set'
# [Sample code]
# list_1 = [1,2,2,3,3,3,4,5,6]
# set_1 = set(list_1) # change list_1 to set_1. The redundant ones will be removed.
# print(set_1) # {1, 2, 3, 4, 5, 6}

# (J.3) Values / Memory Address
# [Descrition]  Demostration for show the values and memory address.
# [Sample code]
# set_1 = {1,1,2}
# set_2 = {1,2}
# print(f"address for set_1 = {id(set_1)}, set_2 = {id(set_2)}") # Different address
# print(f"values for set_1 = {set_1}, set_2 = {set_2}") # Same values (set_1 = {1, 2}, set_2 = {1, 2})

# (J.4) Immutable
# [Descrition]  Demostration for immutable operation.
# [Sample code]
# set_1 = {"str_1", "str_2", "str_3"}
# print(f"set_1={set_1}, address={id(set_1)}") # set_1={'str_1', 'str_2', 'str_3'}, address=1891129918848
# set_1.add("str_4") # Use built-in method add() to add new set element.
# print(f"set_1={set_1}, address={id(set_1)}") # set_1={'str_1', 'str_2', 'str_3', 'str_4'}, address=1891129918848
# set_1[0] = "str_5" # TypeError: 'set' object does not support item assignment (Immutable)

# (J.5) Built-in Methods
# [Descrition]  A set of bulit-in methods used by set
# [Note] Refer as https://www.w3schools.com/python/python_ref_set.asp

#############################################################################
# Compare "==" and "is"
# a. "==" means Value 
# b. "is" means Memory Address
#############################################################################
list_1 = []
list_2 = []
print(f"list_1={id(list_1)}")
print(f"list_2={id(list_2)}")

if list_1 == list_2:
    print("list_1 and list_2 had the same value.")
else:
    print("list_1 and list_2 had the different value.")

if list_1 is list_2:
    print("list_1 and list_2 pointed the same Memory Address.")
else:
    print("list_1 and list_2 pointed the different Memory Address.")
    
#############################################################################
# Object (show values and memory status)
#############################################################################
# a = 5
# b = 6
# sum = a + b
# print(id(a))
# print(id(b))
# print(id(sum))

#############################################################################
# object (demo 1)
#############################################################################
# a = 10
# b = a
# print(a, id(a)) # 10 2031121558096
# print(b, id(b)) # 10 2031121558096 (address b: pointed to same as a)
# b = 15
# print(a, id(a)) # 10 2031121558096
# print(b, id(b)) # 15 2031121558256 (address b: changed)
# b = b + 5
# print(b, id(b)) # 20 2031121558416 (address b: changed again)

#############################################################################
# object demo 2 (mutable)
#############################################################################
# dict_1 = {} # init dictionary
# set_1 = set() # init set 
# print(type(dict_1)) # <class 'dict'>
# print(type(set_1)) # <class 'set'>
# print(id(dict_1)) 
# dict_2 = dict_1 # dict_2 and dict_1 pointed the same dict object(which means same memory address)
# dict_2['name'] = "Gino"
# print(f"dict_1={dict_1}, dict_2={dict_2}") # dict_1 and dict_2 has the same content {'name': 'Gino'}
# print(f"address dict_1={id(dict_1)}, dict_2={id(dict_2)}") # dict_1 and dict_2 still points the same memory address.

#############################################################################
# object demo 3 (immutable)
#############################################################################
# a = 0
# print(id(a))
# b = a
# print(id(b))
# b = 2
# print(id(b))

#############################################################################
# exceptions
#############################################################################
# try:
#     marks = 10000
#     a = marks / 0 # Divisor is 0. It will cause an exception.
#     print(a)
# except Exception as e:
#     print("Exception catched --> {}".format(e)) # e = division by zero

