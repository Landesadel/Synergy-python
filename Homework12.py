#Ex1
class Transport(object):
    name = ''
    max_speed = 0
    mileage = 0
    seating_capacity = 0

    def __init__(self, name, max_speed, mileage, seating_capacity = 50):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = seating_capacity

    def get_info(self):
        return f"Название автомобиля: {self.name}. Скорость: {self.max_speed}. Пробег: {self.mileage}"

    def get_seating_capacity(self):
        return f"Вместимость одного автобуса {self.name}: {self.seating_capacity} пассажиров"

bus = Transport('Renaul Logan', 180, 12)

print(bus.get_info())

#Ex2

bus = Transport('Renaul Logan', 180, 12)

print(bus.get_seating_capacity())