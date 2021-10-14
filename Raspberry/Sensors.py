from sense_hat import SenseHat

class SensorController:
    def __init__(self) -> None:
        self.sense = SenseHat()

    def clear_sense(self):
        self.sense.clear()

    def get_pressure(self):
        self.clear_sense()
        return self.sense.get_pressure()

    def get_temperature(self):
        self.clear_sense()
        return self.sense.get_temperature()

    def get_humidity(self):
        self.clear_sense()
        return self.sense.get_humidity()

    def get_acceleration(self):
        self.clear_sense()
        return self.sense.get_accelerometer_raw()