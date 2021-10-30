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

# def devide(x, y):
#     if (y == 0):
#         return None
#     return x / y;
#
#
# result = devide(create_question("enter numerator", int), create_question("enter denominator", int));
#
# print(f"result = {result}")

# 2

def user_info(name="name", surname="surname", city="city", birthday="birthday", email="email", phone="phone"):
    print(
        f"{surname} {name} lives in the city of {city} was born on the {birthday}. Phone number-{phone}, email-{email}")


print(
    'query #2: user_info(email="test@test.ru",phone="99-99-99",name="Alex",surname="Smith",city="London",birthday="1987-01-19")')
user_info(email="test@test.ru", phone="99-99-99", name="Alex", surname="Smith", city="London", birthday="1987-01-19")


# 3

def biggest_sum(x, y, z):
    list = [x, y, z];
    list.sort(reverse=True)
    return list[0] + list[1]


print('answer:biggest_sum(10,2,7)=', biggest_sum(10, 2, 7))


# 4

def array_exponent(x, y):
    if y < 0:
        return x ** y
    result = 1
    for i in range(y):
        result = result * x
    return result


print('array_exponent(3,0)=', array_exponent(3, 0))
print('array_exponent(3,3)=', array_exponent(3, 3))


# 5


# 6 я так понял юзать title не льзя

def title_word(word):
    if len(word) > 0:
        return "".join([word[:1].upper(), word[1:]])
    return word


def custom_title(fraze):
    return " ".join([title_word(k) for k in fraze.split(" ")])


print("custom_title('test word fraze 1-num')=", custom_title('test word fraze 1-num'))
