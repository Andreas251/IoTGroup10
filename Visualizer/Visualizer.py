import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib
import requests
import datetime as dt

url = 'https://localhost:44340/'
sensor_endpoint = url + 'api/Sensor/Sensors'


def set_reading_type():
    user_inputs = {
        "type_of_reading": "",
        "sensor_id": "",
        "latest": "", # y/n
        "latest_by_sensor": "", # y/n
        "start_time": "",
        "end_time": ""
    }

    print('--- Types of available readings ---\n')
    print('- Accelerometer \n')
    print('- Airpressure \n')
    print('- Humidity \n')
    print('- Temperature \n')
    print('-----------------------------------\n')
    user_inputs["type_of_reading"] = input('Input desired reading: ').lower()

    user_inputs["latest"] = input('Do you want latest data? (y/n): ').lower() # check input

    if user_inputs["latest"].lower() == "n":
        user_inputs["start_time"] = input('Input desired start time of reading: ').lower() # check input
        user_inputs["end_time"] = input('Input desired end time of reading: ').lower() # check input

    user_inputs["latest_by_sensor"] = input('Do you want data from a specific sensor? (y/n): ').lower() # check input

    if user_inputs["latest_by_sensor"].lower() == "y":
        response = requests.get(sensor_endpoint, verify=False).json()
        x = 1

        for i in response:
            print(str(x) + ": " + str(i))
            x = x + 1

        chosen_sensor_id = input('Input desired sensor: ')
        user_inputs["sensor_id"] = response[chosen_sensor_id - 1]

    return user_inputs


def get_reading(user_inputs):
    endpoint = "/api"
    params = {}

    endpoint = endpoint + "/" + user_inputs["type_of_reading"]
    if user_inputs["latest"].lower() == "y":
        if user_inputs["latest_by_sensor"].lower() == "y":
            endpoint = endpoint + "/LatestBySensor"
            params["sensorId"] = user_inputs["sensor_id"]
        else:
            endpoint = endpoint + "/Latest"
    else:
        endpoint = endpoint + "/ReadingsByTime"
        params["sensorId"] = user_inputs["sensor_id"]
        params["start"] = user_inputs["start_time"]
        params["end"] = user_inputs["end_time"]

    #structure of the get parameters
    # params = {
    #     'sensorId' : 'E34D3937-65D5-4DE1-A80E-E29F998D8967',
    #     'start' :  '2021-11-03 13:41:25.9502560',    #dt.datetime.now() - dt.timedelta(minutes = 40),
    #     'end' :   '2021-11-03 13:41:29.9502490'      #dt.datetime.now()
    # }

    response = requests.get(url + endpoint, params=params, verify=False)
    
    return response.json()


def convert_timestamp_format(timestamp):
    """
    Converts timestamp from string of C# DateTimeOffset received from the API to Python datetime.
    """
    timestamp = timestamp.replace("T", " ")
    timestamp = timestamp.split("+")
    dt_date = dt.datetime.strptime(timestamp[0], "%Y-%m-%d %H:%M:%S.%f")
    return dt_date


def convert_dataformat(data_collection, data_type):
    """
    data_collection: array of readings of a certain type, e.g. temperatureReadings[].
    data_type: the type of reading, e.g. "temperature".
    """
    data = []
    timestamps = []
    
    for i in data_collection:
        if data_type.lower() == "accelerometer":
            speed = calculate_speed([i["x"], i["y"], i["z"]], i["timestamp"])
            data.append(speed)
        else:
            data.append(i[data_type])

        dt_date = convert_timestamp_format(i["timestamp"])
        timestamp = matplotlib.dates.date2num(dt_date)
        timestamps.append(timestamp)

    return data, timestamps


def calculate_speed(data, timestamp):
    """
    Calculating movement based on accelerometer data and returning plottable data.
    """
    raise NotImplementedError


def plot_reading(reading, timestamps, data_type: str):
    ax = plt.subplots()
    ax.plot(timestamps, reading)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
    plt.xticks(rotation=10)
    plt.xlabel("Time")
    plt.ylabel(data_type.capitalize())
    plt.show()


def main():
    user_inputs = set_reading_type()
    response = get_reading(user_inputs)
    data, timestamp = convert_dataformat(response, user_inputs["type_of_reading"])
    plot_reading(data, timestamp, user_inputs["type_of_reading"])


if __name__ == "__main__":
    main()