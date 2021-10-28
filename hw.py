def create_question(question, type):
    try:
        return type(input(question.strip() + " "))
    except ValueError as e:
        print("Ошибка: не корректно введено значение")
        create_question(question, type)


# 1

example_string = "example_string"
example_number = 100

print(example_string,example_number,sep="\n")

user_name = create_question(question="what is your name?",type=str)
user_age = create_question(question="how old are you?",type=int)

print(user_name,user_age,sep=" age:")

# 2

seconds_count = create_question(question="How many secconds?",type=int)

def zero_first(num):
    if(num<10):
        return f"0{num}"
    return f"{num}"

houres = seconds_count//3600
minutes = (seconds_count - houres*3600)//60
seconds = seconds_count - houres*3600 - minutes*60;

print(f"{zero_first(houres)}:{zero_first(minutes)}:{zero_first(seconds)}")

# 3
user_number = create_question(question="get number?", type=int)
print(int(f"{user_number}") + int(f"{user_number}{user_number}") + int(f"{user_number}{user_number}{user_number}"))

#4
user_number4 = create_question(question="get number?", type=int)
biggest_num = 0
for c in f"{user_number4}":
    if biggest_num == 9:
        break
    next_int = int(c)
    if next_int > biggest_num:
        biggest_num = next_int
print("Max number is:", biggest_num)

# 5

proceeds = create_question("What proceeds?", int)
costs = create_question("What costs?", int)
profit = proceeds - costs;

if profit > 0:
    print("прибыль — выручка больше издержек")
    rent = profit / proceeds
    print("рентабельность выручки {0:.2f}".format(rent))
    count_workers = create_question("Count workers?", int)
    print("рибыль фирмы в расчете на одного сотрудника {0:.2f}".format( rent / count_workers))
else:
    print("убыток — издержки больше выручки")

# 6

initial_distance = create_question("What distance first day?", int)
need_distance = create_question("What distance need in day?", int)
day = 1


def print_distance():
    print("{0}-й день: {1:.2f}".format(day, initial_distance))


print_distance()
while initial_distance < need_distance:
    initial_distance += (initial_distance * 0.1)
    day += 1
    print_distance()
