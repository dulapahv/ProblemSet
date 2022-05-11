with open('cat.jpg', 'rb') as f:
    data = f.read()
    print(data.hex())