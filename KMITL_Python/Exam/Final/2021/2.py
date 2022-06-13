popularity_scores = {"c++": 99.7, "c": 96.7, "Java": 97.5, 
                    "Python": 100, "C#": 89.4}

def get_rankings(scores):
    return dict(sorted(scores.items(), key=lambda element: element[1],
                reverse=True))

print(get_rankings(popularity_scores))