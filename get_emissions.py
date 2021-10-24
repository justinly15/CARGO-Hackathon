def calculate_emissions(distance, mode, mass):
    if mode == 'air' or mode == 'Air':
        #1.404g/kg*km
        emissions_rate = 1.404
    elif mode == 'rail' or mode == 'Rail':
        # .0157
        emissions_rate = .0157
    # default to ground transport?
    else:
        # 1.650g/kg*km with 1.417 scalar for detour index
        # (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3835347/)
        # 1.164 without
        emissions_rate = 1.65

    # g CO2/product = km * g C02/km * kg * kg/product
    result = float(distance) * float(emissions_rate) * float(mass)
    # accurate to 1 gram
    formatted_result = "{:.0f}".format(result)
    return formatted_result
