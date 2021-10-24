def calculate_emissions(distance, mode, mass):
    if mode == 'air':
        emissions_rate = 1
    else:
        emissions_rate = 1
    # kg CO2/product = km * kg C02/km * kg/product
    result = int(distance) * int(emissions_rate) * int(mass)
    result = str(result)
    return result + 'kg'
