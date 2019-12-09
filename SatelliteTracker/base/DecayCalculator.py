class DecayCalculator:
    density_model = ""
    current_altitude = 0
    def init(self,alt):
        print("hello")
        self.current_altitude = alt;
        self.get_density_model_at_alt()

    def get_density_model_at_alt(self):
        print(self.current_altitude)
