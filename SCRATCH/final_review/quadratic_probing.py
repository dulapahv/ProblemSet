# create a list of numbers
random_list = [17, 65, 91, 45, 18, 74, 62, 84, 32]

# create a hash table of size 11
hash_table = [None] * 11

# hash each number in the list and insert it into the hash table
for i in random_list:
    pos = i % 11
    c1 = 1
    c2 = 1
    while True:
        if hash_table[pos] is None:
            hash_table[pos] = i
            break
        else:
            pos = (pos + c1 * c2) % 11
            c2 += 1

# print the hash table
print(hash_table)