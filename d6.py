"""Write a function called user_name that generates a username
from the user’s email. The code should ask the user to input an
email and the code should return everything before the @ sign
as their user name. For example, if someone enters
ben@gmail.com, the code should return ben as their user
name."""


def user_name(email_1: str) -> str:
    user = email_1.split('@', 1)
    return user[0]


mail = "antoine@gmail.com"
user_name(mail)

"""Write a function called zeroed code that takes a list of numbers
as an argument. The code should zero (0) the first and the last
number in the list. For example, if the input is [2, 5, 7, 8, 9],
your code should return [0, 5, 7, 8, 0]."""


def zeroed_func(int_list: list[int]) -> list[int]:
    print(int_list)
    int_list[0] = 0
    int_list[len(int_list)-1] = 0
    return int_list


lis_1 = [5, 2, 3, 6, 9, 4]

print(zeroed_func(lis_1))
