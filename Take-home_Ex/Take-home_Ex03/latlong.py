
import googlemaps
import pandas as pd

addresses = pd.read_csv("Proximity_to_good_primary_school.csv")

gmaps = googlemaps.Client(key = 'This_is_my_API_key')
addresses['lat'] = None
addresses['long'] = None

for x in range(len(addresses)):
    geocode_result = gmaps.geocode(addresses.loc[x, 'Address'])
    try:
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        addresses.loc[x,'Lat'] = lat
        addresses.loc[x,'Lon'] = lng
    except:
        lat = None
        lng = None

addresses.to_csv('address_coords.csv')
