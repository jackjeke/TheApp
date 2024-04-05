result={'items': [{'title': 'Gaborone, Botswana', 'id': 'here:cm:namedplace:26683504', 'resultType': 'locality', 'localityType': 'city', 'address': {'label': 'Gaborone, Botswana', 'countryCode': 'BWA', 'countryName': 'Botswana', 'state': 'Gaborone', 'city': 'Gaborone'}, 'position': {'lat': -24.65527, 'lng': 25.91904},
                   'mapView': {'west': 25.82347, 'south': -24.76656, 'east': 26.02378, 'north': -24.51259}, 'scoring': {'queryScore': 1.0, 'fieldScore': {'city': 1.0}}}]}



lat=result['items'][0]['position']['lat']
lon=result['items'][0]['position']['lng']

print(lat)
print(lon)
