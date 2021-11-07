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
    
    user_input = ''
    type_of_reading = ''

    print('--- Types of available readings ---\n')
    print('- Accelerometer \n')
    print('- Airpressure \n')
    print('- Humidity \n')
    print('- Temperature \n')
    print('-----------------------------------\n')
    user_input = input('Input desired reading: ').lower()
    
    if(user_input == 'accelerometer'):
        type_of_reading = endpoints['_accReading']
    elif(user_input == 'airpressure'):
        type_of_reading = endpoints['_airReading']
    elif(user_input == 'humidity'):
        type_of_reading = endpoints['_humReading']
    elif(user_input == 'temperature'):
        type_of_reading = endpoints['_tmpReading']
    else:
        type_of_reading = 'default'

    return type_of_reading


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


def convert_datetime(date_time):
    date_time = date_time.replace("T", " ")
    date_time = date_time.split("+")
    return date_time[0]


def convert_humidity_dataformat(data):
    humidity = []
    dates = []
    
    for i in data:
        humidity.append(i["humidity"])
        converted = convert_datetime(i["timestamp"])
    
        dt_date = dt.datetime.strptime(converted, "%Y-%m-%d %H:%M:%S.%f")
        date = matplotlib.dates.date2num(dt_date)
        
        dates.append(date)

    return humidity, dates


def plot_reading(reading, dates):
    fig, ax = plt.subplots()
    ax.plot(dates, reading)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
    plt.xticks(rotation=10)
    plt.xlabel("Time")
    plt.ylabel("Humidity")
    plt.show()


def get_data():
    data = [
        {
            "id": 0,
            "timestamp": "2021-11-07T08:59:46.90102+01:00",
            "humidity": 0,
            "sensorId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        },
        {
            "id": 0,
            "timestamp": "2021-11-07T09:59:46.90102+01:00",
            "humidity": 1,
            "sensorId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        }
    ]
    return data


def main():
    #set_reading_type()

    data = get_data()

    # data = get_reading('tis')
    humidity, dates = convert_humidity_dataformat(data)
    plot_reading(humidity, dates)
    
    return 0



if __name__ == "__main__":
    main()