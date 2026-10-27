from opencage.geocoder import OpenCageGeocode
import pprint

def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        query = city
        results = geocoder.geocode(query)
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(results)
        if results:
            lat = round(results[0]['geometry']['lat'],2)
            lng = round(results[0]['geometry']['lng'], 2)
            return f'Широта: {lat}, Долгота: {lng}'
        else:
            return 'Город не найден'
    except Exception as err:
        return f'Ошибка'


key = '96112fb6d80d4059ae9dabea94898600'
city = 'Ялта'
coordinates = get_coordinates(city, key)
print(coordinates)


