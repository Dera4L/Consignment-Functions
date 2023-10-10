from geopy.geocoders import Nominatim

def address_to_coordinates(address):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(address)
    
    if location:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        return None  # Address not found or other error
    
    

address = "1748 Fairway Drive, Oakland, California"
coordinates = address_to_coordinates(address)

if coordinates:
    latitude, longitude = coordinates
    print(f"Latitude: {latitude}, Longitude: {longitude}")
else:
    print("Address not found or other error occurred.")
