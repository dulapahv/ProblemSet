file, year = input().split(' ')

with open(file, 'r') as f:
    get_data = f.readlines()
    score = []
    for entry in get_data:
        if entry[0] == year[2] and entry[1] == year[3]:
            score.append(float(entry.split(' ')[1]))
    if score:
        print(f'{min(score)} {max(score)} {sum(score)/len(score)}')
    else:
        print('No data')
