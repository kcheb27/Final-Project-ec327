
import requests
import math


def get_closest(building):
    indices = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    values = []
    for i in range(len(building)):
        values.append((building[i].population/building[i].capacity)*10)

    
    # zip the two lists together
    zipped = zip(indices, values)

  # sort the zipped list by the values in the second element of each tuple
    sorted_zipped = sorted(zipped, key=lambda x: x[1])

  # unzip the sorted list and return only the first element (the indices)
    return [x[0] for x in sorted_zipped]




