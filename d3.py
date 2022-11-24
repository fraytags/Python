"""Write a function called register_check that checks how many
students are in school. The function takes a dictionary as a
parameter. If the student is in school, the dictionary says ‘yes’. If
the student is not in school, the dictionary says ‘no’. Your
function should return the number of students in school. Use the
dictionary below. Your function should return 3.
register = {'Michael':'yes','John': 'no',
'Peter':'yes', 'Mary': 'yes'}"""

"""Function that checks if a student is present, from a list"""


def register_check(d_1):
    i = 0
    students = {}
    for e, el in d_1.items():
        if el == "yes":
            students[e] = el
            i = i + 1
    print(f"There are {i} students")
    return students


my_dic = {'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes', 'Tiphaine': 'yes'}
register_check(my_dic)

"""names = ["kerry", "dickson", "John", "Mary",
"carol", "Rose", "adam"]
You are given a list of names above. This list is made up of names
of lowercase and uppercase letters. Your task is to write a code
that will return a tuple of all the names in the list that have only
lowercase letters. Your tuple should have names sorted
alphabetically in descending order. Using the list above, your
code should return:
('kerry', 'dickson', 'carol', 'adam')"""

names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]
a = ()


def check_up_and_sort(names):
    dic = []
    for i in range(len(names)):
        if names[i].islower():
            dic.append(names[i])
    return tuple(dic)


print(check_up_and_sort(names))
