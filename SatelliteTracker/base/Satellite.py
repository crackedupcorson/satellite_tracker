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
            orbital_decay["status"] = "unavailable"
            orbital_decay["decay_date"] = "Unsure"
        else:
            orbital_decay["status"] = "calculating"
            orbital_decay["decay_date"] = "TBC"
        return orbital_decay