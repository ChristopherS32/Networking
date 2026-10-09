def liters_100km_to_miles_gallon(liters):
    miles = 100000 / 1609.344
    gallons = liters / 3.785411784
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    hundred_km = (miles * 1609.344) / 100000
    liters = 1 * 3.785411784
    return liters / hundred_km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))