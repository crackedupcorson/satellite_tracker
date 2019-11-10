from random import randrange

def get_random_cat_id():
    return randrange(45)

#We're defining low earth orbit as less than 2000km
LOW_EARTH_ORBIT_LIMIT = 2000
ATMOSPHERIC_UPPER_LIMIT = 500
ATMOSPHERIC_LOWER_LIMIT = 180

def get_decade_from_year(launch_year):
    decade_decay = ""
    if 1950 <= launch_year <= 1959:
        decade_decay = LaunchDecadeWithDecayPercentage.FIFTIES
        print("Satellite is from the 50s, launched {}".format(launch_year))
    elif 1960 <= launch_year <= 1969:
        decade_decay = LaunchDecadeWithDecayPercentage.SIXTIES
        print("Satellite is from the 60s, launched {}".format(launch_year))
    elif 1970 <= launch_year <= 1979:
        decade_decay = LaunchDecadeWithDecayPercentage.SEVENTIES
        print("Satellite is from the 70s, launched {}".format(launch_year))
    elif 1980 <= launch_year <= 1989:
        decade_decay = LaunchDecadeWithDecayPercentage.EIGHTIES
        print("Satellite is from the 80s, launched {}".format(launch_year))
    elif 1990 <= launch_year <= 1999:
        decade_decay = LaunchDecadeWithDecayPercentage.NINETIES
        print("Satellite is from the 90s, launched {}".format(launch_year))
    elif 2000 <= launch_year <= 2009:
        decade_decay = LaunchDecadeWithDecayPercentage.NOUGHTS
        print("Satellite is from the 00s, launched {}".format(launch_year))
    elif 2010 <= launch_year <= 2019:
        decade_decay = LaunchDecadeWithDecayPercentage.TWENTIES
        print("Satellite is from the 10s, launched {}".format(launch_year))
    return decade_decay


def generate_decay_percentage():
    return randrange(100)

def calculate_atmospheric_density(sat_altitude):
    print("get atmospheric density at a given altitude ")

def calculate_atmospheric_temperature(sat_altitude):
    print("get atmospheric temperature at a given altitude")

class LaunchDecadeWithDecayPercentage():
    FIFTIES = "1950s"
    SIXTIES = "1960s"
    SEVENTIES = "1970s"
    EIGHTIES = "1980s"
    NINETIES = "1990s"
    NOUGHTS = "2000s"
    TENS = "2010s"
    TWENTIES = "2020s"


def get_initial_orbit_params():
    print ("getting initial orbit params")