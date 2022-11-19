"""
In here we will create the customers that are interested in using the cars.

This function will be called from the main Epoch function when it decides to add
another customer and make them book the vehicle.

"""
import datetime
import random
import numpy as np

class Customer():

    def __init__(self, date_time: datetime.datetime):
        self.id = random.randint(1, 4294967295)
        self.start_date = date_time + datetime.timedelta(days=random.randint(0,5))
        self.end_date = self.start_date + datetime.timedelta(days=random.randint(0,5))
        # Middle of Munich is N48.145 ±0.065, E11.450 ±0.15
        self.start_N = np.random.normal(0.0, 0.025, 1)
        self.start_N += 48.145
        self.Start_E = np.random.normal(0.0, 0.055, 1)
        self.Start_E += 11.450
        # And generate the destination of the customer
        self.End_N = np.random.normal(0.0, 0.025, 1)
        self.End_N += 48.145
        self.End_E = np.random.normal(0.0, 0.055, 1)
        self.End_E += 11.450

        # Select a car from the database
        # Select Start: Sixt S_168 Munich Central Train Station (DE)
        # Select End: S_5254 Munich Stachus (City) (DE)


