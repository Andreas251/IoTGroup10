from enum import Enum
from time import sleep
import json
import datetime

from Sensors import SensorController
from MqttClient import MqqtClient

class TopicURI(Enum):
    Root = "iot_grp10"
    TemperatureURI =    Root + "/temp"
    HumidityURI =       Root + "/humidity"
    AirPressureURI =    Root + "/airpressure"
    AccelerometerURI =  Root + "/accelerometer"
    GyroscopeURI =      Root + "/gyroscope"
    MagnetometerURI =   Root + "/magnetometer"

class Measurement:
    def __init__(self, identifier, val) -> None:
        self.timestamp = str(datetime.datetime.now())
        #self.identifier = identifier
        self.value = val

def main():
    # Sensors
    sensors = SensorController()
    client = MqqtClient()

    while(True):
        temp = Measurement("Temperature", sensors.get_temperature())
        pressure = Measurement("AirPressure", sensors.get_pressure())
        humidity = Measurement("Humidity", sensors.get_humidity())
        accel = Measurement("Acceleration", sensors.get_acceleration())

        print()
        print(f"Temp: {temp}")
        print(f"Pressure: {pressure}")
        print(f"Humidity: {humidity}")
        print(f"Acceleration: {accel}")
        print("\nPublishing data\n")

        # TODO: QOS er altid 0, kan ændres hvis ønsket (forhåbentligt)
        client.publish(TopicURI.TemperatureURI.value, json.dumps(temp.__dict__))
        client.publish(TopicURI.AirPressureURI.value, json.dumps(pressure.__dict__))
        client.publish(TopicURI.HumidityURI.value, json.dumps(humidity.__dict__))
        client.publish(TopicURI.AccelerometerURI.value, json.dumps(accel.__dict__))
        sleep(60)
        #TODO man kunne styre pi'en gennem en subscribtion p /iout_grp10/rpi_commands



    print("\nGOODBYE\n")
    return 0

if __name__ == "__main__":
    main()













