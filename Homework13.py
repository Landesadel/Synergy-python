import math

#Ex1
class Cashbox(object):
    cash = 0

    def __init__(self) -> None:
        pass

    def __init__(self, cash):
        self.cash = cash

    def top_up(self, amount):
        self.cash += amount

    def count_1000(self):
        return self.cash // 1000
    
    def take_away(self, amount):
        if self.cash >= amount:
            self.cash -= amount
        else:
            print('Недостаточно денег в кассе.')

cashbox = Cashbox(100)
cashbox.top_up(5000)
print(cashbox.count_1000())
cashbox.take_away(2000)
print(cashbox.count_1000())
cashbox.take_away(6000)

#Ex2
class Turtle(object):
    point_x = 0
    point_y = 0
    __step_size = 1

    def __init__(self, point_x, point_y):
        self.point_x = point_x
        self.point_y = point_y

    def go_up(self):
        self.point_y += self.__step_size

    def go_down(self):
        self.point_y -= self.__step_size

    def go_left(self):
        self.point_x -= self.__step_size

    def go_right(self):
        self.point_x += self.__step_size

    def evolve(self):
        self.__step_size += 1

    def degrade(self):
        if self.__step_size > 1:
            self.__step_size -= 1
        else:
            print('Размер шага не может быть меньше или равняться 0')

    def count_moves(self, x, y):
        diff_x = abs(x - self.point_x)
        diff_y = abs(y - self.point_y)
        
        return math.ceil((diff_x + diff_y) / self.__step_size)
    
turtle = Turtle(2, 4)

print(turtle.count_moves(7, 8))
turtle.degrade()
turtle.evolve()
print(turtle.count_moves(7, 8))
