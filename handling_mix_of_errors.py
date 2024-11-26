try:
    result = "5" + 5
except TypeError as e:
    print(f"TypeError: {e}")

try:
    num = int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

try:
    my_list = [10,20,30]
    print(my_list[5])
except IndexError as e:
    print(f"IndexError: {e}")

try:
    my_dict = {"a":1, "b":2}
    print(my_dict["c"])
except KeyError as e:
    print(f"KeyError: {e}")

try:
    division = 10/0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

'''
Shuffling except lines means the program will end up crashing
and won't continue to run any other functions
'''
