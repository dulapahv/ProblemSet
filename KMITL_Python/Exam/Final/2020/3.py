def find_route_distance(destination, route):
    total_dist = 0
    if destination in route.keys():
        total_dist += route.get(destination)[1]
        find_route_distance(route.get(destination)[0], route)
    else:
        return f"{total_dist}."

routes = {"i": ["j", 4.0],
          "a": ["b", 3.4],
          "j": ["k", 6.0],
          "c": ["d", 5.6],
          "b": ["c", 4.0]}

print(f"{find_route_distance('a', routes)}")