import random
import numpy as np


class Car:
    BOOKED = "booked"
    RETURNING = "returning"
    FREE = "free"
    CHARGING = "charging"

    def __init__(self, car_id, state, latitude, longitude, battery_lvl, charging_station_id):
        self.car_id = car_id
        self.latitude = latitude
        self.longitude = longitude
        self.prev_latitude = self.latitude + random.choice([-0.001, 0, 0.001])
        self.prev_longitude = self.longitude + random.choice([-0.001, 0.001])

        self.battery_lvl = battery_lvl
        self.id_charging_station = charging_station_id
        self.state = state

    def update(self, core_instance):

        if self.state == self.BOOKED and random.choice([True, False]):
            latitude, longitude = self.get_position()
            movement_lat, movement_long = self.get_movement_direction()
            new_lat = latitude + movement_lat * (random.random() * 2)
            new_long = longitude + movement_long * (random.random() * 2)

            # updates all necessary values
            self.update_position(new_lat, new_long)
        elif self.state == self.RETURNING:
            # we move the car towards the charging station
            latitude, longitude = self.get_position()
            station_lat, station_long = core_instance.stations[self.id_charging_station].get_position()
            new_lat = ((station_lat - latitude) * random.random() * 2) + latitude
            new_long = ((station_long - longitude) * random.random() * 2) + longitude

            # updates all necessary values
            self.update_position(new_lat, new_long)
        # should be update last
        self.update_state(core_instance)

    def update_state(self, core_instance):
        if self.state == self.BOOKED:
            self.state = np.random.choice([self.BOOKED, self.RETURNING], 1, p=[0.8, 0.2])[0]
            if self.state == self.RETURNING:
                # assign a charging station to the car
                self.id_charging_station = core_instance.find_optimal_station(self.car_id)
                self.attach_to_station(core_instance)
        elif self.state == self.RETURNING:
            # new_state = np.random.choice(["booked", "returning"], 1, p=[0.8, 0.2])[0]
            distance_to_station = core_instance.euclidean_distance(core_instance.fleet[self.car_id].get_position(),
                                                                   core_instance.stations[
                                                                       self.id_charging_station].get_position())
            if distance_to_station < 0.01:
                if self.battery_lvl >= 80.0:
                    self.state = self.FREE
                else:
                    self.state = self.CHARGING
            # else state stays the same
        elif self.state == self.FREE:
            if self.battery_lvl < 80.0:
                self.attach_to_station(core_instance)
                self.state = self.CHARGING
            else:
                self.state = np.random.choice([self.FREE, self.BOOKED], 1, p=[0.8, 0.2])[0]
                if self.state == self.BOOKED:
                    # we remove a car from the station when it gets booked
                    core_instance.stations[self.id_charging_station].detach_from_station(self.car_id)
        elif self.state == self.CHARGING:
            if self.battery_lvl > 95.0:
                self.attach_to_station(core_instance)
                self.state = self.FREE
            else:
                # we keep it the same and charge battery
                self.increase_battery_level(core_instance)

        else:
            raise Exception(f"Car id '{self.car_id}' has an invalid state!")

    def decrease_battery_level(self):
        # update battery
        self.battery_lvl -= 5
        if self.battery_lvl <= 20:
            self.battery_lvl += random.randint(50, 85)

    def increase_battery_level(self, core_instance):
        new_battery_lvl = core_instance.fleet[self.car_id].get_battery_level() + 2.5
        self.battery_lvl = min(new_battery_lvl, 100)

    def update_position(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

        # each time we update the position we decrease the battery
        self.decrease_battery_level()

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

    def get_battery_level(self):
        return self.battery_lvl

    def attach_to_station(self, core_instance):
        # TODO optimize depending on other parameters ->
        suggested_station = core_instance.find_optimal_station(self.car_id)
        # set car station
        self.id_charging_station = suggested_station
        # add car to station
        core_instance.stations[suggested_station].add_to_station(self.car_id)

    def set_position(self, latitude, longitude):
        self.prev_latitude = self.latitude
        self.prev_longitude = self.longitude

        self.latitude = latitude
        self.longitude = longitude

    def get_position(self):
        return self.latitude, self.longitude

    def get_movement_direction(self):
        return self.latitude - self.prev_latitude, self.longitude - self.prev_longitude

    def get_state(self):
        return self.state

    def get_charging_station(self):
        if self.id_charging_station is None:
            return "None"
        return self.id_charging_station