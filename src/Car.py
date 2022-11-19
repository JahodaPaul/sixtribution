import random


class Car:
    def __init__(self, id):
        self.id = id
        self.battery_lvl = random.randint(0, 95)
        self.latitude = random.randint(0, 100)
        self.longitude = random.randint(0, 100)
        self.locked = True
        self.want_to_return = False
        self.id_charging_station = {}

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False

