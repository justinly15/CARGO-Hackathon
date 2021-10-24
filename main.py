import requests
from get_distance import calculate_distance
from get_emissions import calculate_emissions

url = "https://distanceto.p.rapidapi.com/get"

origin = 'Los Angeles'
destination = 'New York'
#mass in kg
mass = 1

if __name__ == '__main__':
    dist = calculate_distance(origin, destination)
    air_emissions = calculate_emissions(dist, 'air', mass)
    ground_emissions = calculate_emissions(dist, 'ground', mass)
    print(air_emissions)
    #
    # TODO:
    #   calculate emissions for both air and ground transport based on emissions rates and product mass
    #
    #