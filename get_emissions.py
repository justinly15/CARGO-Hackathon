def calculate_emissions(distance, mode, mass):
    if mode == 'air':
        emissions_rate = 2
    else:
        emissions_rate = 1

    # kg CO2/product = km * kg C02/km * kg/product
    return int(distance) * int(emissions_rate) * int(mass)
