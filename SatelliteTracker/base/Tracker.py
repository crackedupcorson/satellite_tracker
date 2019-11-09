import n2yo
import sys,os

from satellite_tracker.SatelliteTracker.base import Helpers
from satellite_tracker.SatelliteTracker.base import Satellite

categories = {}

def get_long_lat():
    long_lat = {}
    if len(sys.argv) > 1:
        sys.argv[1] = long_lat
    else:
        longitude = os.getenv("Longitude")
        latitude = os.getenv("Latitude")
        longitude =-6.396430
        latitude = 53.512150
        altitude = 73
        long_lat["longitude"] = longitude
        long_lat["latitude"] = latitude
        long_lat["altitude"] = altitude
        return long_lat


def resolve_categoryname(cat_id):
    return categories[cat_id]

def get_categories_from_file():
    with open('resources/catergories.txt') as f:
        counter = 0
        for line in f:
            categories[str(counter)] = line
            counter = counter + 1

class SatelliteTracker:

    api_key = "QVKMZM-XVQMLB-F9AHJG-47ZM"
    def run(self):
        n2yo_client = self.get_n2y0_client()
        get_categories_from_file()
        cat_id = Helpers.get_random_cat_id()
        self.get_satellites_over_head(90, cat_id)

    def get_n2y0_client(self):
        self.satellite_api_client = n2yo.N2YO(self.api_key)
        print("this gets the N2y0 API and stores it as a global")

    def get_satellites_over_head(self, degree, cat_id):
        get_categories_from_file()
        print("Booting up!")
        long_lat = get_long_lat()
        sats_above_json = self.satellite_api_client.get_above(degree,cat_id,long_lat["latitude"], long_lat["longitude"], long_lat["altitude"])
        sats_above_info = sats_above_json[0]
        current_sat_count = sats_above_info['satcount']
        print("there are {} satellites above your head with a degree specification of {} under category {}".format(current_sat_count,degree,cat_id))
        print("category {} resolves to {}".format(cat_id, categories[str(cat_id)]))
        sats_above = sats_above_json[1]
        self.create_sat_objects(sats_above)

    def create_sat_objects(self, sats_above):
        if(len(sats_above)) > 1:
            for sat in sats_above:
                sat_object = Satellite.Satellite(id = sat["satid"], name= sat["satname"],launch_date=sat["launchDate"], designator=sat["intDesignator"], satlat=sat["satlat"],satlong=sat["satlng"],satalt=sat["satalt"])
                sat_object.get_satellite_decade()


g

if __name__ == "__main__":
    sat_tracker = SatelliteTracker()
    sat_tracker.run()