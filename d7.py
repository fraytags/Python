"""Write a function called string_range that takes a single
number and returns a string of its range. The string characters
should be separated by dots(.) For example, if you pass 6 as
an argument, your function should return ‘0.1.2.3.4.5’."""
import names as names


def string_range(num_1: int) -> str:
    new_str = ""
    for i in range(num_1):
        i = str(i)
        new_str = new_str + i + "."
    return new_str


"""Extra Challenge: Dictionary of names 
You are given a list of names, and you are asked to write a code
that returns all the names that start with ‘S’. Your code should
return a dictionary of all the names that start with S and how
many times they appear in the dictionary. Here is a list below:
names = ["Joseph","Nathan", "Sasha", "Kelly",
"Muhammad", "Jabulani", "Sera”, "Patel", "Sera”]
Your code should return: {“Sasha”: 1, “Sera”: 2}"""


def search_S_names(names_1: list) -> list:
    i = 0
    names_with_s = []
    for n in names_1:
        if str(n).startswith("S"):
            names_with_s.append(n)
    return names_with_s


names = ["Joseph", "Nathan", "Sasha", "Kelly",
         "Muhammad", "Jabulani", "Sera"]
print(search_S_names(names))
