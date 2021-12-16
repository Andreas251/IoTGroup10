import numpy as np

def calculate_min_max_mean(reading: list, timestamps: list):
    """
    Calculation minimum, maximum and mean values for readings used on plots.
    """
    min = [np.amin(reading)]*len(timestamps)
    max = [np.amax(reading)]*len(timestamps)
    mean = [np.mean(reading)]*len(timestamps)
    
    return min, max, mean


def calculate_speed(data, timestamp):
    """
    Calculating movement based on accelerometer data and returning plottable data.
    """
    raise NotImplementedError