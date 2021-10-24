import sys

from get_distance import calculate_distance
from get_emissions import calculate_emissions

url = "https://distanceto.p.rapidapi.com/get"

# script can be run from the command line using 'python3 main.py <origin> <destination> <mass>'
origin = sys.argv[1]
destination = sys.argv[2]
# I made mass an optional argument-- if it isn't supplied, it will default to 1kg (the output will
# represent the emissions generated by moving 1kg from origin to destination)
if len(sys.argv) == 4:
    mass = sys.argv[3]
else:
    mass = 1

if __name__ == '__main__':
    dist = calculate_distance(origin, destination)
    air_emissions = calculate_emissions(dist, 'air', mass)
    ground_emissions = calculate_emissions(dist, 'ground', mass)
    print(str(air_emissions) + 'kg of carbon emissions created')
    #
    # TODO:
    #     0) Use accurate data for calculations
    #     1) Pass air_emissions and ground_emissions to GUI for presentation to user
    #     2) Integrate GUI input with program so that user-specified input is used
    #           a) The program allows for no mass to be specified, in which case it defaults
    #               to 1kg. Frontend can determine whether you want to use it or not.
    #     3) Create documentation (basic README about why we made the tool, what it does,
    #        who it helps, etc.). We can maybe present this README on the site?
    #     4) (if we have time) Creative representation of carbon emissions on webpage
    #
