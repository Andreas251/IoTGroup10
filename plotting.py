import matplotlib.pyplot as plt
import matplotlib
import datetime as dt

def main():
    data = get_data()
    plot_temperature(data)
    

def plot_temperature(data):
    temperatures, dates = convert_dataformat(data)

    plt.plot_date(dates, temperatures)
    plt.xlabel("Time")
    plt.xticks(rotation=10)
    plt.ylabel("Temperature (celsius)")
    plt.show()


def convert_dataformat(data):
    temperatures = []
    dates = []
    
    for i in data:
        temperatures.append(i[0])

        date = matplotlib.dates.date2num(i[1])
        dates.append(date)

    return temperatures, dates


def get_data():
    # Dummy data
    data = []
    data.append([12.42, dt.datetime.now()])
    data.append([13.21, dt.datetime.now()+dt.timedelta(0,10)])
    data.append([12.86, dt.datetime.now()+dt.timedelta(0,20)])
    data.append([14.43, dt.datetime.now()+dt.timedelta(0,30)])
    data.append([15.54, dt.datetime.now()+dt.timedelta(0,40)])
    data.append([15.12, dt.datetime.now()+dt.timedelta(0,50)])
    data.append([14.01, dt.datetime.now()+dt.timedelta(0,60)])
    data.append([15.48, dt.datetime.now()+dt.timedelta(0,70)])
    return data


if __name__ == "__main__":
    main()