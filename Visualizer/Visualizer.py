import matplotlib.pyplot as plt
import requests


url = ''

endpoints = {
    '_accReading' : '',
    '_airReading' : '',
    '_humReading' : '',
    '_tmpReading' : ''
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



#def plot_readings(data):







def main():
    set_reading_type()
    return 0



if __name__ == "__main__":
    main()