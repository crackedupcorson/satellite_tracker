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

    def __init__(self, id, name, launch_date, designator, satlat, satlong, satalt):
        self.sat_id = id
        self.sat_name = name
        self.launch_date = launch_date
        self.designator = designator
        self.satlat = satlat
        self.satlong = satlong
        self.satalt = satalt

    def get_satellite_decade(self):
        # convert the launch date string to an actual date
        #yyyy-mm-dd
         launch_date_time = datetime.strptime(self.launch_date, "%Y-%m-%d")
         launch_year = launch_date_time.year
         print(launch_year)
         Helpers.get_decade_from_year(launch_year)