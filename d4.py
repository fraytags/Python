"""Write a function called only_floats, which takes two
parameters a and b, and returns 2 if both arguments are floats,
returns 1 if only one argument is a float, and returns 0 if neither
argument is a float. If you pass (12.1, 23) as an argument, your
function should return a 1."""


def only_float(a, b) -> int:
    val = 0

    if int(a) != a:
        val += 1

    if int(b) != b:
        val += 1

    return val


def only_float1(c, d) -> int:
    if int(c) == c and int(d) == d:
        return 0
    elif int(c) == c or int(d) == d:
        return 1
    return 2


"""Write a function called word_index that takes one argument,
a list of strings and returns the index of the longest word in the
list. If there is no longest word (if all the strings are of the same
length), the function should return zero (0). For example, the list
below should return 2.
words1 = ["Hate", "remorse", "vengeance"]
And this list below, should return zero (0)
words2 = ["Love", "Hate"]"""
l1 = ["anticonstitutionnellement","Hello", "Gimmes"]


def word_index(lis_1) -> int:
    pos = 0
    i = 0
    max_1 = ""
    for i in range(len(lis_1)):
        if len(lis_1[i]) > len(max_1):
            max_1 = lis_1[i]
            pos = i
    return pos


print(word_index(l1))

"""
def word_index_v1(lis_1):
    max_1 = 0
    index = 0
    count = 0

    for i in range(len(lis_1)):
        if len(lis_1[i]) > max_1:
            max_1 = len(lis_1[i])
            count = 1
            index = i
        elif len(lis_1[i]) == max_1:
            count += 1

    if count == 1:
        return index
    else:
        return 0
"""
"""
lis = ["test", "ok", "vengeance"]
print(word_index_v1(lis))

lis = ["hello", "salut", "test"]
print(word_index_v1(lis))
"""
