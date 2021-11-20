def miles_to_kilometers(miles):
    result = miles * KILOMETERS_PER_MILE
    return result

KILOMETERS_PER_MILE = 1.609
result = miles_to_kilometers(float(input("Enter the distance in miles: ")))
print(f"The distance is {result:.2f} kilometers.")