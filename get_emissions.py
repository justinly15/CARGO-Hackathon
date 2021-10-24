def calculate_emissions(distance, mode, mass):
    if mode == 'air':
        #1.404g/kg*km
        emissions_rate = 1.404
    else:
        # 1.650g/kg*km with 1.417 scalar for detour index
        # (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3835347/)
        # 1.164 without
        emissions_rate = 1.65

    # g CO2/product = km * g C02/km * kg * kg/product
    result = distance * emissions_rate * mass
    # accurate to 2 decimal places
    formatted_result = "{:.2f}".format(result)
    return formatted_result
