import random


class Car:
    def __init__(self, id):
        self.id = id
        self.battery_lvl = random.randint(0, 95)
        self.latitude = random.randint(0, 100)
        self.longitude = random.randint(0, 100)
        self.locked = True
        self.want_to_return = False
        self.is_charging = False
        self.id_charging_station = None

    def update_position(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def update_battery_level(self, battery_level):
        if 100 >= battery_level >= 0:
            self.battery_lvl = battery_level
        else:
            raise Exception(f"Battery level must be between 0 and 100! Car id '{self.id}'")

    def update_lock_status(self, locked):
        # a check to not override the variable at all times which could lead to door unlocking by mistake
        if self.locked != locked:
            self.locked = locked

    def update_wants_to_return(self, wants_to_return):
        if self.want_to_return != wants_to_return:
            self.want_to_return = wants_to_return

    def update_charging_status(self, id_charging_status, is_charging):
        # the station has to be updated before the charging status
        self.update_charging_station(id_charging_status)

        if self.is_charging != is_charging:
            # if you want to start charging, you must be at a station and not charging
            if len(self.id_charging_station.keys()) == 1 and self.is_charging == False:
                self.is_charging = is_charging
            # if you want to stop charging, you must be at a station and
            elif len(self.id_charging_station.keys()) == 1 and self.is_charging == True:
                self.is_charging = is_charging
            else:
                # TODO test for errors
                raise Exception(f"Car {self.id} car cannot start/end charging if not at station!")

    def update_charging_station(self, station_id):
        self.id_charging_station = station_id

