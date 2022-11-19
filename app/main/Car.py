import random


class Car:
    BOOKED = "booked"
    RETURNING = "returning"
    FREE = "free"
    CHARGING = "charging"

    def __init__(self, car_id, state, latitude, longitude, battery_lvl, charging_station_id):
        self.car_id = car_id
        self.latitude = random.randint(0, 100)
        self.longitude = random.randint(0, 100)

        self.battery_lvl = random.randint(0, 95)
        self.id_charging_station = None
        self.state = state

    def update(self, car_dict, core_instance):
        # updates all necessary values
        self.update_position(car_dict["latitude"], car_dict["longitude"])
        self.set_battery_level(car_dict["battery_level"])

        # should be update last # TODO update station capacity
        self.update_state_and_station(car_dict["station_id"], car_dict["state"], core_instance)

    def update_position(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def set_battery_level(self, battery_level):
        if 100 >= battery_level >= 0:
            if battery_level != self.battery_lvl:
                print("Setting battery level to: ", battery_level)
                self.battery_lvl = battery_level
                print("New battery level: ", self.battery_lvl)
                return True
            else:
                return False
        else:
            raise Exception(f"Battery level must be between 0 and 100! Car id '{self.car_id}'")

    def update_state_and_station(self, station_id, state, core_instance):
        # if state changed
        if self.state != state:
            # if the car was booked it can only go to returning
            if self.state == self.BOOKED:
                if state == self.RETURNING:
                    if station_id is not None:
                        self.state = state
                        self.attach_to_station(core_instance)
                    else:
                        raise Exception(f"Car id '{self.car_id}' is booked and can only go to "
                                        f"returning state if it has a charging station id!")
                else:
                    raise Exception(f"Car id '{self.car_id}' was booked and can only go to returning!")
            elif self.state == self.RETURNING:
                if state == self.FREE or state == self.CHARGING:
                    self.state = state
                else:
                    raise Exception(f"Car id '{self.car_id}' was returning and can only go to free or charging!")
            elif self.state == self.FREE:
                if state == self.BOOKED:
                    # car can be booked TODO remove destination
                    self.state = state
                    if station_id is not None:
                        raise Exception(f"Car id '{self.car_id}' was booked and should not have a station_id")
                    self.id_charging_station = None
                elif state == self.CHARGING:
                    # it can also be plugged in
                    self.state = state
                else:
                    raise Exception(f"Car id '{self.car_id}' was free and can only go to booked or charging!")
            elif self.state == self.CHARGING:
                if state == self.BOOKED:
                    # car can be booked TODO remove destination
                    pass
                elif state == self.FREE:
                    # it can also be unplugged preferably if full
                    pass
                else:
                    raise Exception(f"Car id '{self.car_id}' was charging and can only go to booked or free!")
            else:
                raise Exception(f"Car id '{self.car_id}' has an invalid state!")

    # def update_charging_station(self, station_id):
    #     self.id_charging_station = station_id

    def get_battery_level(self):
        return self.battery_lvl

    def attach_to_station(self, core_instance):
        # TODO optimize depending on other parameters ->
        suggested_station = core_instance.find_optimal_station(self.car_id)
        # set car station
        self.id_charging_station = suggested_station
        # add car to station
        core_instance.stations[suggested_station].add_to_station(self.car_id)

    def get_position(self):
        return self.latitude, self.longitude

