def parse_input(qt):
    db = {}
    for i in range(qt):
        item = input()
        tmp_name, tmp_price = "", ""
        for char in item:
            if char.isprintable() and not char.isnumeric():
                tmp_name += char
            elif char.isnumeric():
                tmp_price += char
        if tmp_name[1:-2] not in db:
            db[tmp_name[1:-2]] = int(tmp_price)
        else:
            db[tmp_name[1:-2]] += int(tmp_price)
    return db


manga_db = parse_input(int(input()))
sale_db = parse_input(int(input()))

total = 0
top = 0
for item in sale_db:
    if item in manga_db:
        total += sale_db[item] * manga_db[item]
        if sale_db[item] * manga_db[item] > top:
            top = sale_db[item] * manga_db[item]
if total == 0:
    print('No manga sales')
else:
    top_manga = []
    print(f'Total manga sales: {total:.1f}')
    print('Top sales:')
    for item in sale_db:
        if item in manga_db:
            if sale_db[item] * manga_db[item] == top:
                top_manga.append(item)
    print(*sorted(top_manga), sep='\n')
