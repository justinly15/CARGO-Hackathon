def calculate_emissions(distance, mode, mass):
    if mode == 'air':
        emissions_rate = 1
    else:
        emissions_rate = 1
    return distance * emissions_rate * mass
