"""Write a function called convert_add that takes a list of strings
as an argument and converts it to integers and sums the list. For
example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and
summed to 9.

"""


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

"""Function which checks if there are some duplicates"""


def check_duplicates(list_1):
    names = ['Yoda', 'Moses', 'Joshua', 'Mark']
    print(list_1)
    for i in range(len(list_1)):
        for j in range(len(names)):
            if list_1[i] == names[j]:
                print(f"There are some duplicates in the dictionnary {list_1[i]}")
            else:
                print("No duplicates")

"""
ask the user to enter some random words
something to try later : create a file, read the content and compare it from the list
"""
names = ['Yoda', 'Moses', 'Joshua', 'Mark']
check_duplicates(names)
