from datetime import datetime

from satellite_tracker.SatelliteTracker.base import Helpers


class Satellite:
    sat_id = 0
    sat_name = ""
    launch_date = ""
    designator = ""
    satlat = 0
    satlong = 0
    satalt = 0
    launch_decade = 0

    def __init__(self, id, name, launch_date, designator, satlat, satlong, satalt):
        self.sat_id = id
        self.sat_name = name
        self.launch_date = launch_date
        self.designator = designator
        self.satlat = satlat
        self.satlong = satlong
        self.satalt = satalt

    def set_satellite_decade(self):
        # convert the launch date string to an actual date
        #yyyy-mm-dd
         launch_date_time = datetime.strptime(self.launch_date, "%Y-%m-%d")
         launch_year = launch_date_time.year
         print(launch_year)
         self.launch_decade = Helpers.get_decade_from_year(launch_year)

    def set_satellite_decay(self):
        orbital_decay = {}
        # todo - this takes the decade, altitude and longlat and attempts to estimate the orbital decay
        # the most contributing factor is how they interact with the atmosphere. Right now this function will be limited to LEO satellites
        if self.satalt >= Helpers.LOW_EARTH_ORBIT_LIMIT:
            print("Satellite is above LEO")
            orbital_decay["status"] = "unavailable"
            orbital_decay["decay_date"] = "Unsure"

        else:
            orbital_decay["status"] = "calculating"
            orbital_decay["decay_date"] = "TBC"
            if Helpers.ATMOSPHERIC_LOWER_LIMIT >= self.satalt <= Helpers.ATMOSPHERIC_UPPER_LIMIT:
                print("Atmospheric density can be applied")
                self.calculate_orbital_decay()
            else:
                print("Satellite is not in a decaying orbit")
        return orbital_decay

    def calculate_orbital_decay(self):
        #todo build funtion to calculate orbital decay for a satellite in LEO
        #Get the original orbit params which can be used to determine decay from the till now - can use this to help build the model of when it will fully decay
        Helpers.get_initial_orbit_params()
        #Get the cross sectional area of the satellite to calculate drag
        Helpers.get_cross_sectional_area()
        #Get the atmospheric density at the given altitude, which helps calculate drag
        Helpers.calculate_atmospheric_density(self.satalt)
        #Get the atmospheric temperature at the given altitude which will helps calculate the atmospheric model
        Helpers.calculate_atmospheric_temperature((self.satalt))

        #Using atmospheric density and temperature we can make an atmospheric model to use in calculating drag/decay
        print("starting calculation for  orbital decay")