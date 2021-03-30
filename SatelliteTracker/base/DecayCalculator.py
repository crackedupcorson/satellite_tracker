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
