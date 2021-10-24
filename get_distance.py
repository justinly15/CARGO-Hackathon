import requests

url = "https://distanceto.p.rapidapi.com/get"

headers = {
    'x-rapidapi-host': "distanceto.p.rapidapi.com",
    'x-rapidapi-key': "b6db550ea5msh7d4bafe03228fd2p19473bjsnfebe72fb5aeb"
}


# This function takes in two strings describing locations, an origin and a destination, and calls on
# a map API to find the straight-line distance between these two points, which is then returned.
def calculate_distance(origin, destination):
    # Construct querystring for API call
    originString = f'{origin}'
    destString = f'{destination}'

    querystring = {"route": "[{\"t\":\"Boston\"}, {\"t\":\"Providence\"}]", "car": "false", "foot": "false"}
    querystring['route'] = '[{\"t\":\"' + originString + '\"}, {\"t\":\"' + destString + '\"}]'

    # Make API call and store response
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.text

    # split response string to return only the info we care about (haversine distance)
    result = response.find('haversine')
    return float(response[result + 11:result + 17])
