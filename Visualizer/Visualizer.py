import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib
import requests
import datetime as dt

url = 'https://localhost:44340/'

endpoints = {
    '_accReading' : 'api/',
    '_airReading' : 'api/',
    '_humReading' : 'api/Humidity/Readings',
    '_tmpReading' : 'api/'
}




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
        #Print sensors
        user_inputs["sensor_id"] = input('Input desired sensorId: ').lower()

    
    

    
    

    return user_inputs


def get_reading(input):
    
    #structure of the get parameters
    params = {
        'sensorId' : 'E34D3937-65D5-4DE1-A80E-E29F998D8967',
        'start' :  '2021-11-03 13:41:25.9502560',    #dt.datetime.now() - dt.timedelta(minutes = 40),
        'end' :   '2021-11-03 13:41:29.9502490'      #dt.datetime.now()
    }

    response = requests.get(url + endpoints['_humReading'],params=params, verify=False)
    print(dt.datetime.now())
    print(response.status_code)
    print(response.json())
    
    return response.json()


def convert_timestamp_format_old(date_time): # TODO: Remove when new works
    date_time = date_time.replace("T", " ")
    date_time = date_time.split("+")
    return date_time[0]


def convert_humidity_dataformat(data): # TODO: Remove when general function works
    humidity = []
    dates = []
    
    for i in data:
        humidity.append(i["humidity"])
        converted = convert_timestamp_format_old(i["timestamp"])
    
        dt_date = dt.datetime.strptime(converted, "%Y-%m-%d %H:%M:%S.%f")
        date = matplotlib.dates.date2num(dt_date)
        
        dates.append(date)

    return humidity, dates


def convert_timestamp_format(timestamp): # TESTED - With Humidity
    """
    Converts timestamp from string of C# DateTimeOffset received from the API to Python datetime.
    """
    timestamp = timestamp.replace("T", " ")
    timestamp = timestamp.split("+")
    dt_date = dt.datetime.strptime(timestamp[0], "%Y-%m-%d %H:%M:%S.%f")
    return dt_date


def convert_dataformat(data_collection, data_type): # TESTED - With Humidity
    """
    data_collection: array of readings of a certain type, e.g. temperatureReadings[].
    data_type: the type of reading, e.g. "temperature".
    """
    data = []
    dates = []
    
    for i in data_collection:
        if data_type.lower() == "accelerometer":
            data.append([i["x"], i["y"], i["z"]])
        else:
            data.append(i[data_type])

        dt_date = convert_timestamp_format(i["timestamp"])
        date = matplotlib.dates.date2num(dt_date)
        dates.append(date)

    return data, dates


def calculate_movement(data, dates):
    """
    Calculating movement based on accelerometer data and returning plottable data.
    """
    raise NotImplementedError


def plot_reading(reading, dates):
    fig, ax = plt.subplots()
    ax.plot(dates, reading)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
    plt.xticks(rotation=10)
    plt.xlabel("Time")
    plt.ylabel("Humidity")
    plt.show()


def main():
    endpoint, reading = set_reading_type()

    data = get_reading(endpoint)
    humidity, dates = convert_dataformat(data,reading)
    plot_reading(humidity, dates)
    
    return 0



if __name__ == "__main__":
    main()