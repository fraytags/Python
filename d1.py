from math import *

"""Day 1: Division and Square-root
Write a function called divide_or_square that takes one
argument (a number), and returns the square root of the number
if it is divisible by 5, returns its remainder if it is not divisible by
5. For example, if you pass 10 as an argument, then your function
should return 3.16 as the square root.
"""
"""Function which answers to the previous statement of the day"""


def divide_or_square(number):
    # a number is divisible by 5 if the result of the division ends with 0 or 5.
    res = str(number / 5)
    # We check if the chain ends with 0 or 5 = is divisible by 5
    if res.endswith(str(0)) or res.endswith(str(5)):
        res = sqrt(number)
        return res
    else:
        res = number % 5
        return res


print(divide_or_square(25))

"""
Extra Challenge: Longest Value
Write a function called longest_value that takes a dictionary
as an argument and returns the first longest value of the
dictionary. For example, the following dictionary should return
– apple as the longest value.
fruits = {'fruit': 'apple', 'color': 'green'}"""

dic = {'fruit': 'test', 'color': 'green'}


def longest_value(dic):
    w_len_max = ""
    for i in range(len(dic.values())):
        if len(i) > len(w_len_max):
            w_len_max = i
    return w_len_max


print(f"The longest value of the chain in input is the word : {longest_value(dic)}")
