from json import detect_encoding
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib
import requests
import datetime as dt
import urllib3
import matplotlib.animation as animation
import numpy as np
urllib3.disable_warnings()

url = 'https://localhost:44340/'
sensor_endpoint = url + 'api/Sensor/Sensors'
valid_sensors = ("temperature", "airpressure", "humidity", "accelerometer")


def set_reading_type():
    user_inputs = {
        "type_of_reading": "",
        "sensor_id": "",
        "latest": "", # y/n
        "latest_by_sensor": "", # y/n
        "start_time": "",
        "end_time": "",
        "live_update" : ""
    }

    print('--- Types of available readings ---\n')
    print('- Accelerometer \n')
    print('- Airpressure \n')
    print('- Humidity \n')
    print('- Temperature \n')
    print('-----------------------------------\n')
    while user_inputs["type_of_reading"].lower() not in valid_sensors:
        user_inputs["type_of_reading"] = input('Input desired reading: ').lower()
        if user_inputs["type_of_reading"].lower() not in valid_sensors:
            print("Invalid value. Was: " + user_inputs["type_of_reading"] + ". Must be one of " + str(valid_sensors))

    while user_inputs["latest"] not in ("y", "n"):
        user_inputs["latest"] = input('Do you want latest data? (y/n): ').lower()
        if user_inputs["latest"] not in ("y", "n"):
            print("Your input was not valid. Must be 'y' or 'n'.")
    
    if user_inputs["latest"].lower() == "y":
        while user_inputs["live_update"] not in ("y", "n"):
            user_inputs["live_update"] = input('Do you want live data? (y/n): ').lower()
            if user_inputs["live_update"] not in ("y", "n"):
                print("Your input was not valid. Must be 'y' or 'n'.")

    if user_inputs["latest"].lower() == "n":
        user_inputs["start_time"] = get_time_input('Input desired start time of reading in format "YYYY-MM-DD HH:MM": ')
        user_inputs["end_time"] = get_time_input('Input desired end time of reading in format "YYYY-MM-DD HH:MM": ')

    while user_inputs["latest_by_sensor"] not in ("y", "n"):
        user_inputs["latest_by_sensor"] = input('Do you want data from a specific sensor? (y/n): ').lower()
        if user_inputs["latest_by_sensor"] not in ("y", "n"):
            print("Your input was not valid. Must be 'y' or 'n'.")

    if user_inputs["latest_by_sensor"].lower() == "y":
        response = requests.get(sensor_endpoint, verify=False)
        response = response.json()
        x = 1

        for i in response:
            print(str(x) + ": " + str(i))
            x = x + 1

        chosen_sensor_id = input('Input desired sensor: ')
        user_inputs["sensor_id"] = response[int(chosen_sensor_id) - 1]
    return user_inputs


def get_time_input(string: str):
    try:
        user_input = input(string).lower()
        dt.datetime.strptime(user_input, '%Y-%m-%d %H:%M')
    except ValueError:
        print("Invalid input")
        user_input = get_time_input(string)
    return user_input


def get_reading(user_inputs):
    endpoint = "api"
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

    if not isinstance(data_collection, list):
        data_collection = [data_collection]

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


def plot_reading(reading, timestamps, data_type: str, sensor_id, plot_mean = False):
    fig, ax = plt.subplots()
    fig.set_size_inches(15,8)
    ax.plot(timestamps, reading, marker=".", label="Reading")
    if plot_mean:
        mean = [np.mean(reading)]*len(timestamps)
        mean_line = ax.plot(timestamps, mean, label='Mean', linestyle='--')
    
    max = [np.amax(reading)]*len(timestamps)
    min = [np.amin(reading)]*len(timestamps)
    max_line = ax.plot(timestamps, max, label='Max', linestyle='--')
    min_line = ax.plot(timestamps, min, label='Min', linestyle='--')
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xticks(rotation=10)
    plt.xlabel("Time")
    plt.ylabel(data_type.capitalize())
    plt.title(data_type.capitalize() + " Reading\nSensor ID: " + str(sensor_id),pad=10, fontsize=12, fontweight='demibold')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), frameon=False)
    plt.show()


def init_animation():
    plt.title("Live " + animation_input["type_of_reading"].capitalize() + " Reading")
    plt.plot(animated_x,animated_y)
    plt.ylabel(animation_input["type_of_reading"].capitalize())
    plt.xlabel("Time of Reading")
    plt.xticks(rotation=10)


def animate(i):
    response = get_reading(animation_input)
    sensor_id = response["sensorId"]

    if not response['id'] in last_response:

        last_response[0] = response['id']
        print(response)

        data, timestamp = convert_dataformat(response, animation_input["type_of_reading"])
        

        animated_x.append(timestamp)
        animated_y.append(data)

        print(animated_y)

        plt.cla()
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.ylabel(animation_input["type_of_reading"].capitalize(), labelpad=5)
        plt.xlabel("Time of Reading", labelpad=5)
        plt.xticks(rotation=10)

        plt.title("Live " + animation_input["type_of_reading"].capitalize() + " Reading\nSensor ID: " + str(sensor_id), pad=10, fontsize=12, fontweight='demibold')

        plt.plot(animated_x,animated_y, marker = 'o', label='Reading')

        mean = [np.mean(animated_y)]*len(animated_x)
        max = [np.amax(animated_y)]*len(animated_x)
        min = [np.amin(animated_y)]*len(animated_x)
            
        mean_line = plt.plot(animated_x, mean, label='Mean', linestyle='--')
        max_line = plt.plot(animated_x, max, label='Max', linestyle='--')
        min_line = plt.plot(animated_x, min, label='Min', linestyle='--')

        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), frameon=False)


def main():
    user_inputs = set_reading_type()

    if user_inputs["live_update"].lower() == 'y' and user_inputs["latest"].lower() == 'y':
        global animation_input
        global animated_x
        global animated_y
        global last_response
        last_response = [0]
        animated_x = []
        animated_y = []
        animation_input = user_inputs
        live_dat = animation.FuncAnimation(plt.gcf(), animate,init_func=init_animation, interval=30000)
        plt.gcf().set_size_inches(15,8)
        plt.show()
    else:
        response = get_reading(user_inputs)
        sensor_id = response[0]["sensorId"]

        data, timestamp = convert_dataformat(response, user_inputs["type_of_reading"])
        plot_reading(data, timestamp, user_inputs["type_of_reading"], sensor_id, plot_mean=True)


if __name__ == "__main__":
    main()