from geopy.geocoders import Nominatim


def get_country_from_coordinates(latitude, longitude, language="ru"):
    # Create a geolocator object with a user agent
    geolocator = Nominatim(user_agent="your_app_name")

    # Get location based on coordinates
    location = geolocator.reverse((latitude, longitude), exactly_one=True)
    if location and 'country' in location.raw['address']:
        location = geolocator.geocode(location.raw['address']['country'], language=language)
        return str(location)
    return None
