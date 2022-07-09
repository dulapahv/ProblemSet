node = {"A": ["B", 3.4],
		"C": ["D", 5.6],
		"B": ["C", 4.0],
		"D": ["E", 4.2],
		"E": ["F", 5.5],
		"G": ["H", 2.3],
		"I": ["J", 3.3],
		"F": ["G", 6.0],
		"H": ["I", 3.9],
		"J": [None, 0.0]}


def find_route(start, node):
	nodeTravelled = []
	dist = 0
	while True:
		if start in node.keys() and start is not None:
			dist += node.get(start)[1]
			nodeTravelled += start
			start = node.get(start)[0]
		else:
			break
	return f'{nodeTravelled}, {dist:.2f} km.'


exec(input())
