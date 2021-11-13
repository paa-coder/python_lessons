import time


# 1
class TrafficLight:
    def __init__(self):
        self.__color = None

    def start(self) -> None:
        self.__to_red()

    def __to_red(self) -> None:
        self.__color = "red"
        self.__sleep(7)
        self.__to_yellow()

    def __to_yellow(self) -> None:
        self.__color = "yellow"
        self.__sleep(2)
        self.__to_green()

    def __to_green(self) -> None:
        self.__color = "green"
        self.__sleep(4)
        self.__color = None

    def __sleep(self, count):
        print(self.__color)
        for x in range(1, count + 1):
            print(x, end=",")
            time.sleep(1)
        print("")


tl = TrafficLight()
tl.start()


# 2
class Road:
    def __init__(self, lenght, width):
        self.__length = lenght
        self.__width = width
        self.__weight = 25
        self.__thick = 5

    def common_weight(self) -> int:
        return self.__length * self.__width * self.__weight * self.__thick


r = Road(5000, 20)
print(r.common_weight())


# 3
class Worker:
    def __init__(self, name="name", surname="surname", position="position", wage=600, bonus=800):
        self._name = name
        self._surname = surname
        self._position = position
        self._sums = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self) -> str:
        return f"{self._surname} {self._name}"

    def get_total_income(self) -> int:
        return self._sums["wage"] + self._sums["bonus"]


p = Position()

print(p.get_full_name())
print(p.get_total_income())


# 4
class Car:
    def __init__(self, speed=20, color="red", name=None, is_police=False):
        self.speed = speed
        self.color = color
        self.position = name
        self.is_police = is_police

    def go(self):
        print("go")

    def stop(self):
        print("stop")

    def turn(self, diretion):
        print(f"turn on {diretion}")

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def __init__(self, speed=60, color="red"):
        super().__init__(speed, color, "TownCar")

    def show_speed(self):
        if self.speed > 60:
            return "сообщение о превышении скорости"
        return self.speed


class SportCar(Car):
    def __init__(self, speed=80, color="red"):
        super().__init__(speed, color, "SportCar")


class WorkCar(Car):
    def __init__(self, speed=40, color="WorkCar"):
        super().__init__(speed, color, "SportCar")

    def show_speed(self):
        if self.speed > 40:
            return "сообщение о превышении скорости"
        return self.speed


class PoliceCar(Car):
    def __init__(self, speed=100):
        super().__init__(speed, color="blue", name="PoliceCar", is_police=True)


spc = SportCar()
print(spc.show_speed())
wc = WorkCar()
print(wc.show_speed())
wc.speed = 100
print(wc.show_speed())


# 5

class Stationery:
    def __init__(self, title=""):
        self._title = title

    def draw(self):
        return f"Запуск отрисовки.{self._title}"


class Pen(Stationery):
    def __init__(self) -> None:
        super().__init__(title="Pen")


class Handle(Stationery):
    def __init__(self) -> None:
        super().__init__(title="Handle")


class Pencil(Stationery):
    def __init__(self) -> None:
        super().__init__(title="Pencil")


print(Stationery().draw())
print(Pen().draw())
print(Handle().draw())
print(Pencil().draw())
