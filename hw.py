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

# 1

list_types = [1, 1.1, "1", [1, 1], {1, 1}, (1, 1)];
for i in list_types:
    print(type(i))

# 2

list_elements = [];

while True:
    list_elements.append(create_question("add element", str))
    if exit("quite from list creating?"):
        break

first_list_elements = list_elements[0::2]
second_list_elements = list_elements[1::2]

for i in range(len(second_list_elements)):
    first_list_elements.insert(i*2,second_list_elements[i])

print("init list:", list_elements)
print("result list:", first_list_elements)

# 3

mouths_list = ["зима", "зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима"]
mouths_dick = {"12": "зима","1": "зима", "2": "зима", "3": "весна", "4": "весна", "5": "весна", "6": "лето", "7": "лето",
               "8": "лето", "9": "осень", "10": "осень", "11": "осень" }

month=None
while month not in range(1,13):
    month=create_question("insert month",int)

print("period from list",mouths_list[month-1])
print("period from dict",mouths_dick[f"{month}"])


#4

words = create_question("enter text",str).split();
for i in range(len(words)):
    print(f"word №{i+1} - {words[i][:10]}")

#5

rating_list = [7, 5, 3, 3, 2]

while True:
    rating_list.append(create_question("add element", int))
    rating_list.sort(reverse=True)
    print("updated rating:",rating_list)
    if exit("quite from rate creating?"):
        break

#6

products = []

while True:
    product_number = create_question("product number",str)
    specifications = {}

    specifications["name"] = create_question("product name",str)
    specifications["cost"] = create_question("product cost",str)
    specifications["count"] = create_question("product count",str)
    specifications["unit"] = create_question("product unit",str)

    products.append((product_number,specifications))
    if exit("quite from products creating?"):
        break

print("itog list",products)

group_specification = {}

def group_supplier(field_name):
    group_specification[field_name] = list(set(x[1][field_name] for x in products))

group_supplier("name")
group_supplier("cost")
group_supplier("count")
group_supplier("unit")

print("itog specification",group_specification)



