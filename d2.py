"""Write a function called convert_add that takes a list of strings
as an argument and converts it to integers and sums the list. For
example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and
summed to 9.

"""
from array import *

"""function that converts str as int and sum all the content of the list once converted as integer"""


def convert_add(st_2):
    sum_1 = 0
    for i in range(len(st_2)):
        st_2[i] = int(st_2[i])
        sum_1 = sum_1 + st_2[i]
    return sum_1

st_2 = ["5", "12", "52", "21"]
print(convert_add(st_2))

"""
Extra Challenge: Duplicate Names
Write a function called check_duplicates that takes a list of
strings as an argument. The function should check if the list has
any duplicates. If there are duplicates, the function should return
the duplicates. If there are no duplicates, the function should
return "No duplicates". For example, the list of fruits below
should return apple as a duplicate and list of names should
return "no duplicates".
fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']"""

def check_duplicates(st_3, st_4):

    for i in range(len(st_3)):
        if