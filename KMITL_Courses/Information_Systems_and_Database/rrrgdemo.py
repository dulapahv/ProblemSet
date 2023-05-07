# we usin the worst database ever, sqlite3
import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('data.db')

# Create a cursor, it's like a pointer to the database
cursor = connection.cursor()

# we buildin a simple table
# we use IF NOT EXISTS so we don't have to worry about the table already exists
create_table = "CREATE TABLE IF NOT EXISTS people (id integer primary key, first_name text, last_name text)"

# while we at it, we can also create a table for the items
# real is a float in SQLlite. I don't know! i use Postgres!
create_table_items = "CREATE TABLE IF NOT EXISTS items (id integer primary key, name text, price real)"

# we execute the query
cursor.execute(create_table)
cursor.execute(create_table_items)

# we can insert data into the table
insert_hitagi = "INSERT INTO people VALUES (1, 'Hitagi', 'Senjougahara')"
cursor.execute(insert_hitagi)

# we can insert multiple data into the table
people = [
    # note that we use a tuple to store the data # best girl btw
    (2, 'Tsubasa', 'Hanekawa'),
    (3, 'Mayoi', 'Hachikuji'),
    (4, 'Suruga', 'Kanbaru'),
    (5, 'Nadeko', 'Sengoku'),
    (6, 'Karen', 'Araragi'),
    (7, 'Tsukihi', 'Araragi'),
    (8, 'Shinobu', 'Oshino'),
    (9, 'Meme', 'Oshino'),
    (10, 'Deishu', 'Kaiki'),
    (11, 'Izuko', 'Gaen'),
    (12, 'Yozuru', 'Kagenui'),
    (13, 'Yotsugi', 'Ononoki'),
    (14, 'Ougi', 'Oshino'),
    (15, 'Tooe', 'Gaen'),  # yo read zoku owarimonogatari yet?
]

# we use executemany to insert multiple data. it can read tuples, lists, and dictionaries
cursor.executemany("INSERT INTO people VALUES (?, ?, ?)", people)

# or just use for loops and string formatting. works too

morepeople = [
    (16, 'John', 'Price'),
    (17, 'Soap', 'MacTavish'),
    (18, 'Simon', 'Riley'),
    (19, 'Kyle', 'Garrick'),
    (20, 'Alejandro', 'Vargas'),
    (21, 'Kate', 'Laswell')
]

for person in morepeople:
    execution = "INSERT INTO people VALUES ({}, '{}', '{}')".format(
        person[0], person[1], person[2])
    cursor.execute(execution)

# albeit this is not recommended. it's prone to SQL injection.
# https://xkcd.com/327/
# https://bobby-tables.com/python

# i forgot to mention that the execute method can also take just a single tuple. it works too. easier too.
cursor.execute("INSERT INTO people VALUES (?, ?, ?)", (22, "Madoka", "Kaname"))

# I forgot about the items table. let's add some items
items = [
    (1, 'Ramen', 100),
    (2, 'Bread', 50),
    (3, 'Coffee', 150),
    (4, 'Tea', 100),
    (5, 'Soda', 100),
    (6, 'Water', 50),
    (7, 'M4A1', 1000),
    (8, 'AK-47', 1000),
    (9, 'Saiga 12 with Dragon Breath', 7000),
    # no recoil, no quill, look at that it can do a very long shot
    (10, 'B&T APC556 tuned by wzstats.gg', 2500),
    (11, 'Gunship Killstreak', 20000),
    (12, 'Juggernaut Killstreak', 15000),
    (13, 'Tactical Nuke Killstreak', 25000),
    (14, 'Love', 2.21),
]

cursor.executemany("INSERT INTO items VALUES (?, ?, ?)", items)

# after we did some significant work, lets commit the changes
connection.commit()

# you said that you use a different table for one to many relationship? let's try it

cursor.execute("CREATE TABLE item_ownership(id integer primary key autoincrement not null, user_id integer, item_id integer, foreign key (user_id) references people(id), foreign key (item_id) references items(id))")

# hanekawa has a.... APC556?
# 2 is hanekawa's id, 10 is the id of the APC556
cursor.execute("INSERT INTO item_ownership VALUES (1, 2, 10)")
# captain price might be thirsty
# 16 is price's id, 3 is the id of the coffee
cursor.execute("INSERT INTO item_ownership VALUES (2, 16, 3)")
# and he might be hungry too
# 16 is price's id, 2 is the id of the bread
cursor.execute("INSERT INTO item_ownership VALUES (3, 16, 2)")
# maybe kaiki also have the APC556?
# 10 is kaiki's id, 10 is the id of the APC556
cursor.execute("INSERT INTO item_ownership VALUES (4, 10, 10)")
# nah, he's too cheap for that. he has a saiga 12 with dragon breath
cursor.execute("DELETE FROM item_ownership WHERE id = 4 AND item_id = 10")
# 10 is kaiki's id, 9 is the id of the saiga 12 with dragon breath
cursor.execute("INSERT INTO item_ownership VALUES (4, 10, 9)")
# maybe he also has a gunship killstreak?
# 10 is kaiki's id, 11 is the id of the gunship killstreak
cursor.execute("INSERT INTO item_ownership VALUES (5, 10, 11)")
# ghost has one too
# 18 is ghost's id, 11 is the id of the gunship killstreak
cursor.execute("INSERT INTO item_ownership VALUES (6, 18, 11)")
# in nise, hachikuji mentioned that she found love on sale for 298 yen
# 3 is hachikuji's id, 14 is the id of love
cursor.execute("INSERT INTO item_ownership VALUES (7, 3, 14)")
# but we all know nadeko is one crazy girl
# 5 is nadeko's id, 13 is the id of the tactical nuke killstreak
cursor.execute("INSERT INTO item_ownership VALUES (8, 5, 13)")

connection.commit()  # don't forget

# maybe we can use user input to insert data into the table?
# we can use the input() function to get user input

# we can use a while loop to keep asking for input

while True:
    print("Enter your data. Enter 'done' to stop")
    id = input("Enter your id: ")

    if id == 'done':
        connection.commit()
        break
    if id.isnumeric() == False:  # be robust!
        print("Invalid input. Please enter a number")
        continue
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    cursor.execute("INSERT INTO people VALUES (?, ?, ?)",
                   (id, first_name, last_name))
# try Robert'); DROP TABLE people;-- as the first name. it will delete the people table. this is called SQL injection
# https://xkcd.com/327/
# but i fixed that by shoving all the user input into the second argument of the execute method

# we can also use the fetchone() function to get the first row of the result as a tuple
cursor.execute("SELECT * FROM people")
print(cursor.fetchone())

# we can also use the fetchall() function to get all the rows of the result as a list of tuples
cursor.execute("SELECT * FROM people")
print(cursor.fetchall())

# we can also use the fetchmany() function to get a specific number of rows of the result as a list of tuples
cursor.execute("SELECT * FROM people")
print(cursor.fetchmany(3))

# let's see the whole table

cursor.execute("SELECT * FROM people")
print("People:")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM items")
print("Items:")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM item_ownership")
print("Item Ownership:")
for row in cursor.fetchall():
    print(row)

# how can we forget about actually selecting data from the table?
# will return Karen and Tsukihi.
cursor.execute("SELECT * FROM people WHERE last_name = 'Araragi")
cursor.execute("SELECT * FROM items where price > 1000")
# fetching gives you a list of tuples. so do as you wish with it.
# or just ORM it. it's easier


# when we're done, we can close the connection
connection.close()

# this SQL in high-level programming language is cool and all, but you know what's even cooler? Object Relational Mapping (ORM).
