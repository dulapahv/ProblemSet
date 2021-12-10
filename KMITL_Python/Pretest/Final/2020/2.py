def find_route(destination, route):
    nodeTravelled = []
    total_dist = 0
    while True:
        if destination in route.keys():
            total_dist += route.get(destination)[1]
            destination = route.get(destination)[0]
            nodeTravelled.append(destination)
        else:
            break
    return f"({nodeTravelled}, {total_dist})."

routes = {"i": ["j", 4.0],
          "a": ["b", 3.4],
          "j": ["k", 6.0],
          "c": ["d", 5.6],
          "b": ["c", 4.0]}

print(f"{find_route('a', routes)}")