import matplotlib.pyplot as plt
import matplotlib
import requests


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
    response = requests.get(url + endpoints['_humReading'], verify=False)
    print(response.status_code)
    print(response.json())
    # return response.json()

    dummy_data = [
        {
            "id": 0,
            "timestamp": "2021-11-03T12:11:42.501Z",
            "humidity": 0,
            "sensorId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        },
        {
            "id": 0,
            "timestamp": "2021-11-03T12:12:42.501Z",
            "humidity": 1,
            "sensorId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        },
        {
            "id": 0,
            "timestamp": "2021-11-03T12:13:42.501Z",
            "humidity": 2,
            "sensorId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        },
    ]
    return dummy_data


def convert_humidity_dataformat(data):
    print(data)
    humidity = []
    dates = []
    
    for i in data:
        humidity.append(i["humidity"])
        print(humidity)

        date = matplotlib.dates.date2num(i["timestamp"])
        dates.append(date)

    return humidity, dates


def plot_reading(humidity, dates):

    plt.plot_date(dates, humidity)
    plt.xlabel("Time")
    plt.xticks(rotation=10)
    plt.ylabel("Humidity")
    plt.show()


def main():
    #set_reading_type()
    data = get_reading('tis')
    humidity, dates = convert_humidity_dataformat(data)
    plot_reading(humidity, dates)

    return 0



if __name__ == "__main__":
    main()