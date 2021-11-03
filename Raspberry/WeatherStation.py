from enum import Enum
from time import perf_counter, sleep
import json
import datetime
import uuid

from Sensors import SensorController
from MqttClient import MqqtClient

#### Averages over 19 minutes
# Avg time awake: 0.08890010573663619
# Avg duty cycle: 0.0014816684289439368
# measurement format in mqtt: {"timestamp": "2021-10-27 09:30:12.172813", "value": 34.1219596862793}

class TopicURI(Enum):
    Root = "iot_grp10"
    TemperatureURI =    Root + "/temp"
    HumidityURI =       Root + "/humidity"
    AirPressureURI =    Root + "/airpressure"
    AccelerometerURI =  Root + "/accelerometer"
    GyroscopeURI =      Root + "/gyroscope"
    MagnetometerURI =   Root + "/magnetometer"

class Measurement:
    def __init__(self, sensor_id, val) -> None:
        self.sensorId = sensor_id
        self.timestamp = str(datetime.datetime.now())
        self.value = val

def main():
    # Sensors
    sensor_id = str(uuid.uuid4())
    sensors = SensorController()
    client = MqqtClient()
    period = 60

    cum_runtime = 0
    cum_duty_cycle = 0
    loops = 0

    while(True):

        t0 = perf_counter()
        
        ### Measure
        temp = Measurement(sensor_id , sensors.get_temperature())
        pressure = Measurement(sensor_id, sensors.get_pressure())
        humidity = Measurement(sensor_id, sensors.get_humidity())
        accel = Measurement(sensor_id, sensors.get_acceleration())

        # TODO: QOS er altid 0, kan ændres hvis ønsket (forhåbentligt)
        ### Publish
        client.publish(TopicURI.TemperatureURI.value, json.dumps(temp.__dict__))
        client.publish(TopicURI.AirPressureURI.value, json.dumps(pressure.__dict__))
        client.publish(TopicURI.HumidityURI.value, json.dumps(humidity.__dict__))
        client.publish(TopicURI.AccelerometerURI.value, json.dumps(accel.__dict__))

        t1 = perf_counter()

        runtime = t1 - t0
        loops += 1

        duty_cycle = runtime / period
        cum_duty_cycle += duty_cycle
        avg_duty_cycle = cum_duty_cycle / loops

        cum_runtime += runtime    
        avg_runtime = cum_runtime / loops

        # Getting data for the report.
        print(f"Time awake: {runtime}, average: {avg_runtime}")
        print(f"Duty cycle: {duty_cycle}, average:{avg_duty_cycle}")
        print()
        sleep(period - runtime)

    print("\nGOODBYE\n")
    return 0
if __name__ == "__main__":
    main()






