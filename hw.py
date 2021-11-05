from functools import reduce
from math import factorial


def create_question(question, type):
    try:
        return type(input(question.strip() + " "))
    except ValueError as e:
        print("Ошибка: не корректно введено значение")
        create_question(question, type)


def exit(question):
    answer = None
    while answer not in ["y", "n"]:
        if answer != None:
            print("accept only y or n")
        answer = create_question(f"{question} [y/n]:", str)

    return answer == "y"


# 2

def filter_biggest_list(list_numbers):
    return (list_numbers[x] for x in range(1, len(list_numbers)) if list_numbers[x] > list_numbers[x - 1])


print(
    'query #2: filter_biggest_list([x for x in filter_biggest_list([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55])])')
print(f"result = {[x for x in filter_biggest_list([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55])]}")

# 3
print('answer:[x for x in range(20,241) if x%20==0 or x%21==0]=',
      [x for x in range(20, 241) if x % 20 == 0 or x % 21 == 0])


# # 4
def unique(arr):
    return [x for x in arr if arr.count(x) == 1]


print('answer:unique([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11])=',
      unique([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]))

# # 5
print('answer:reduce(lambda l,r:l*r,[x for x in range(100,1001,2)])=',
      reduce(lambda l, r: l * r, [x for x in range(100, 1001, 2)]))


# 7 я так понял юзать title не льзя


def factorial_generator(number):
    for x in range(1, number + 1):
        yield factorial(x)


print('query: for x in factorial_generator(14)')
for x in factorial_generator(14):
    print(x)
