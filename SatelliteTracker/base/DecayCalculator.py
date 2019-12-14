class DecayCalculator:
    density_model = ""
    altitude_temperature = 0
    current_altitude = 0
    def init(self,alt):
        print("hello")
        self.current_altitude = alt
        self.altitude_temperature = self.get_temp_at_altitude()
        self.get_density_model_at_alt()

    def get_density_model_at_alt(self):
        print(self.current_altitude)

    def get_temp_at_altitude(self):
        if(self.current_altitude < 5):
            print("It's gonna crash!")
        elif(self.current_altitude > 50):
            print("Any day now")
        elif(self.current_altitude > 1000):
            print("I dunno")
            return 5
        else:
            return 10