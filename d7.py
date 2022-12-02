"""Write a function called string_range that takes a single
number and returns a string of its range. The string characters
should be separated by dots(.) For example, if you pass 6 as
an argument, your function should return ‘0.1.2.3.4.5’."""


def string_range(num_1: int) -> str:
    new_str = ""
    for i in range(num_1):
        i = str(i)
        new_str = new_str + i + "."
    return new_str


print(string_range(6))
