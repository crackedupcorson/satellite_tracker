from random import randrange



def get_random_cat_id():
    return randrange(45)


def get_decade_from_year(launch_year):
    if 1950 <= launch_year <= 1959:
        print("Satellite is from the 50s, launched {}".format(launch_year))
    elif 1960 <= launch_year <= 1969:
        print("Satellite is from the 60s, launched {}".format(launch_year))
    elif 1970 <= launch_year <= 1979:
        print("Satellite is from the 70s, launched {}".format(launch_year))
    elif 1980 <= launch_year <= 1989:
        print("Satellite is from the 80s, launched {}".format(launch_year))
    elif 1990 <= launch_year <= 1999:
        print("Satellite is from the 90s, launched {}".format(launch_year))
    elif 2000 <= launch_year <= 2009:
        print("Satellite is from the 00s, launched {}".format(launch_year))
    elif 2010 <= launch_year <= 2019:
        print("Satellite is from the 10s, launched {}".format(launch_year))


