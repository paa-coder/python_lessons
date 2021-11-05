import os
from re import sub
import json
import pandas as pd
from functools import reduce


def create_question(question, type=str):
    try:
        return type(input(question.strip() + " "))
    except ValueError as e:
        print("Ошибка: не корректно введено значение")
        create_question(question, type)


root = os.path.dirname(__file__)
encoding = "utf-8"


def get_doc_dir():
    docs = os.path.join(root, "docs")
    os.makedirs(docs, exist_ok=True)
    return docs


def line_worker(file, worker) -> int:
    count = 0
    while line := file.readline():
        worker(count, line)
        count += 1
    return count


# 1
def writer():
    with open(os.path.join(get_doc_dir(), "question1.txt"), "w", encoding=encoding) as file:
        while s := create_question("new line").strip() != "":
            print(s, file=file)


writer()
# 2

with open(os.path.join(get_doc_dir(), "question2.txt"), encoding=encoding) as file:
    x = lambda count, line: print(
        'in line № {0} {1} words'.format(count + 1,
                                         len([x for x in sub("[^\sa-zA-Zа-яA-Я0-9]", "", line).split() if x != ""])))
    print('count lines in file = ', line_worker(file, x))

# 3
with open(os.path.join(get_doc_dir(), "question3.txt"), encoding=encoding) as file:
    data = pd.read_csv(file, sep=";", names=['name', 'salary'])
    print("salary>20000", data[data.salary >= 20000].name.tolist())
    print("middle salary = ", data.salary.mean())

# 4
with open(os.path.join(get_doc_dir(), "question4.txt"), encoding=encoding) as file:
    dict = {
        "One": "Один",
        "Two": "Два",
        "Three": "Три",
        "Four": "Четыре"
    }
    data = file.read()
    for k, v in dict.items():
        data = data.replace(k, v)
    with open(os.path.join(get_doc_dir(), "question4_copy.txt"), "w", encoding=encoding) as copy:
        copy.write(data)

# 5
with open(os.path.join(get_doc_dir(), "question5.txt"), "w", encoding=encoding) as file:
    file.write(" ".join([f"{x}" for x in range(25)]))
with open(os.path.join(get_doc_dir(), "question5.txt"), encoding=encoding) as file:
    print("sum of question5.txt = ", reduce(lambda l, r: l + r, [int(x) for x in file.read().split(" ")]))

# 6
with open(os.path.join(get_doc_dir(), "question6.txt"), encoding=encoding) as file:
    data = pd.read_csv(file, sep=" ", names=['name', 'lec', "lab", "p"])


    def to_int(x):
        num = sub("[^0-9]", "", x)
        return int(num) if num != "" else 0


    def cleaner(x):
        if x.name == 'name':
            return [sub("[^\sa-zA-Zа-яA-Я0-9]", "", z) for z in data.name]
        return [to_int(z) for z in data[x.name]]


    data = data.apply(cleaner)

    dict = {}
    for _, row in data.iterrows():
        dict[row["name"]] = row['lec'] + row['lab'] + row["p"]

with open(os.path.join(get_doc_dir(), "question7.txt"), encoding=encoding) as file:
    data = pd.read_csv(file, sep=" ", names=["name", "ownership", "proceeds", "costs"])

    data['profit'] = data.apply(lambda row: row['proceeds'] - row['costs'], axis=1)

    firm_profits = {}
    for _, row in data.iterrows():
        firm_profits[row["name"]] = row["profit"]

    results = [firm_profits, {"average_profit": data[data.profit > 0].profit.mean()}]
    with open(os.path.join(get_doc_dir(), "question7.json"), 'w',encoding=encoding) as outfile:
        json.dump(results, outfile,indent=4)


# from functools import reduce
# from math import factorial
#
#
# def create_question(question, type):
#     try:
#         return type(input(question.strip() + " "))
#     except ValueError as e:
#         print("Ошибка: не корректно введено значение")
#         create_question(question, type)
#
#
# def exit(question):
#     answer = None
#     while answer not in ["y", "n"]:
#         if answer != None:
#             print("accept only y or n")
#         answer = create_question(f"{question} [y/n]:", str)
#
#     return answer == "y"
#
#
# # 2
#
# def filter_biggest_list(list_numbers):
#     return (list_numbers[x] for x in range(1, len(list_numbers)) if list_numbers[x] > list_numbers[x - 1])
#
#
# print(
#     'query #2: filter_biggest_list([x for x in filter_biggest_list([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55])])')
# print(f"result = {[x for x in filter_biggest_list([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55])]}")
#
# # 3
# print('answer:[x for x in range(20,241) if x%20==0 or x%21==0]=',
#       [x for x in range(20, 241) if x % 20 == 0 or x % 21 == 0])
#
#
# # # 4
# def unique(arr):
#     return [x for x in arr if arr.count(x) == 1]
#
#
# print('answer:unique([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11])=',
#       unique([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]))
#
# # # 5
# print('answer:reduce(lambda l,r:l*r,[x for x in range(100,1001,2)])=',
#       reduce(lambda l, r: l * r, [x for x in range(100, 1001, 2)]))
#
#
# # 7 я так понял юзать title не льзя
#
#
# def factorial_generator(number):
#     for x in range(1, number + 1):
#         yield factorial(x)
#
#
# print('query: for x in factorial_generator(14)')
# for x in factorial_generator(14):
#     print(x)
