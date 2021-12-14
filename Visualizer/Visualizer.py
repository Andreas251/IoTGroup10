import visualization_module as visuals
import urllib3
urllib3.disable_warnings()


url = 'https://localhost:44340/'
sensor_endpoint = url + 'api/Sensor/Sensors'
valid_sensors = ("temperature", "airpressure", "humidity", "accelerometer")


def main():
    user_inputs = visuals.get_user_inputs(valid_sensors, sensor_endpoint)

    # user_inputs = { # Used for testing to avoid having to input all the time.
    #     'type_of_reading': 'temperature', 
    #     'sensor_id': 'a9b95020-f72e-498e-987d-a973d4d36972', 
    #     'latest': 'n', 
    #     'latest_by_sensor': 'y', 
    #     'start_time': '2021-12-06 12:00', 
    #     'end_time': '2021-12-06 16:00', 
    #     'live_update': ''
    #     }

    if user_inputs["live_update"].lower() == 'y' and user_inputs["latest"].lower() == 'y':
        visuals.plot_live_data(user_inputs)
    else:
        response = visuals.get_reading(user_inputs, url)
        
        # Response should be a list, so all responses can be handled the same way.
        if not isinstance(response, list):
            response = [response]
        
        # Currently only support for plotting one sensor at the time.
        try:
            sensor_id = response[0]["sensorId"]
        except:
            raise ValueError("Chosen sensor does not exist")

        data, timestamp = visuals.convert_dataformat(response, user_inputs["type_of_reading"])
        visuals.plot_reading(data, timestamp, user_inputs["type_of_reading"], sensor_id)


if __name__ == "__main__":
    main()