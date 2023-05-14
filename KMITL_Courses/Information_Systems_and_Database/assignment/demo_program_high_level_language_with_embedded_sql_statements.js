// JSON vs SQL: A continuation from demo_program_high_level_language_with_embedded_sql_statements.ipynb

// a people array used as a database table for people

people = [
    {
        first_name: "Hitagi",
        last_name: "Senjougahara"
    },
    {
        first_name: "Mayoi",
        last_name: "Hachikuji"
    },
    {
        first_name: "Suruga",
        last_name: "Kanbaru"
    },
    {
        first_name: "Nadeko",
        last_name: "Sengoku"
    },
    {
        first_name: "Tsubasa",
        last_name: "Hanekawa"
    },
    {
        first_name: "Karen",
        last_name: "Araragi"
    },
    {
        first_name: "Tsukihi",
        last_name: "Araragi"
    },
    {
        first_name: "Shinobu",
        last_name: "Oshino"
    },
]

// let's add someone to the table.

// first we create a new person object.
new_person = {
    first_name: "Koyomi",
    last_name: "Araragi"
}

// next we add the object to the end of the array
people.push(new_person)
// anucha top tip: push returns the new length of the array, so you can do people.push(new_person).length to get the new length.


// let's see what it looks like now...
console.log(people)

// now let's say we want to remove someone from the table...
people.pop()
// anucha top tip: pop returns the removed element, so you can do people.pop() to get the removed element.

// for the sake of sanity, lets just add koyomi back in.
people.push(new_person) // ok good

// and see what it looks like now...
console.log(people)

// now let's say we want to print out only the first names of the people in the table...
for (var i = 0; i < people.length; i++) {
    console.log(people[i].first_name)
}

// mass add? no problem
newnamelists = [
    ["Alex", "Mason"],
    ["Frank", "Woods"],
    ["Jason", "Hudson"],
    ["Grigori", "Weaver"],
    ["Joseph", "Bowman"],
]

for (var i = 0; i < newnamelists.length; i++) {
    new_person = {
        first_name: newnamelists[i][0],
        last_name: newnamelists[i][1]
    }
    people.push(new_person)
}

// and see what it looks like now. should have task force 141 in there now.

console.log(people)

//user input? no problem

// first we create a new person object.

new_person = {
    first_name: prompt("What is your first name?"), // prompt() is like input() in python, but for browsers. if you run this in node.js, it will not work.
    last_name: prompt("What is your last name?")
}
//anucha top tip: when you define something, it will return the value of the thing you defined.
//ps. try miho nishizumi or yukari akiyama.

// next we push it
people.push(new_person)

// if you want to add multiple people, use while loops. im too lazy to do it here.

// lets see
console.log(people)

// let's make an item table.

items = [
    {
        name: "Bread",
        price: 2.99,
    },
    {
        name: "Milk",
        price: 3.99,
    },
    {
        name: "Eggs",
        price: 4.99,
    },
    {
        name: "Cheese",
        price: 5.99,
    },
    {
        name: "AN-94",
        price: 999.99,
    },
    {
        name: "AK-12",
        price: 999.99,
    },
    {
        name: "AK-15",
        price: 999.99,
    },
    {
        name: "RPK-16", // sus
        price: 999.99,
    },
    {
        name: "Hunter-Killer Drone",
        price: 9999.99,
    },
    {
        name: "RC-XD",
        price: 99.99,
    },
    {
        name: "Sentry Gun",
        price: 999.99,
    },
    {
        name: "SAM Turret",
        price: 999.99,
    },
    {
        name: "Attack Dogs", // treyarch games doesn't have a tactical nuke, but this is as close as it gets
        price: 9999.99,
    }
]

// let's say we want to print out only the names of the items in the table...
for (var i = 0; i < items.length; i++) {
    console.log(items[i].name)
}

// but how do we link the purchases to the people?

// first: use the same technique as SQL foreign keys. new table that stores the person and item.

// most json serializers will actually copy the value of the object, so we can just use the object itself.

purchasecopyobject = [
    // senjougahara bought bread
    {
        person: people[0],
        item: items[0]
    },
    // nadeko bought the rpk sus
    {
        person: people[3],
        item: items[7]
    },
    // koyomi bought the rcxd
    {
        person: people[8],
        item: items[9]
    },
    // mason bought the attack dogs
    {
        person: people[9],
        item: items[12]
    },
    //the person you inputted bought the hunter killer drone
    {
        person: people[people.length - 1],
        item: items[8]
    }
]

// let's print the whole table
console.log(purchasecopyobject)

// let's print out the first purchase
console.log(purchasecopyobject[0])

// easy, right?
// and what if something is changed in the people table? it will change in the purchase table too.

// let's say senjougahara changed her name to hitagi araragi.
people[0].last_name = "Araragi"

// let's print hitagi's purchase again
console.log(purchasecopyobject[0])
// wtf it changed? yes. because it's the same object.

// but it may not change in some serializers that stores the table as an object, not an array, especially in JSON.
// which makes it a little more complicated.

// the table consists of the whole person and item objects, so we can access the properties of the person and item objects.

// but it takes a lot of space. what about we just store the index of the person and item?

purchaseindex = [
    // senjougahara bought bread
    {
        person: 0,
        item: 0
    },
    // nadeko bought the rpk sus
    {
        person: 3,
        item: 7
    },
    // koyomi bought the rcxd
    {
        person: 8,
        item: 9
    },
    // mason bought the attack dogs
    {
        person: 9,
        item: 12
    },
    //the person you inputted bought the hunter killer drone
    {
        person: people.length - 1,
        item: 8
    }
]
// but where's the id field? my son. we don't need it. the index is the id.

// let's print the whole table
console.log(purchaseindex)

// only numbers, because they are "references" to the actual objects in the people and items array.
// but how do we access the actual objects?

// we can use the index to access the actual objects in the people and items array.

// let's print the first purchase
console.log(purchaseindex[0])
//just numbers? yes. but we can use them to access the actual objects.

// let's print the first purchase's person and the first purchase's item
console.log(people[purchaseindex[0].person], items[purchaseindex[0].item])

// takes a little more work, but it's much more efficient. plus it makes the SQL engineer happy.

// the whole thing changes when we use an object to store a table, just like in firebase. because that's the ONLY reason why firebase is so popular.

peopleobject = {
    0: { // note that we have to define the index ourselves. pretty good for databases. allwos for custom ids.
        first_name: "Hitagi",
        last_name: "Senjougahara"
    },
    1: {
        first_name: "Mayoi",
        last_name: "Hachikuji"
    },
}

// you know what, lets automate this. we're software engineers, not data entry clerks.
// ok alexa play cyberpunk 2077 trailer song

for (var i = 0; i < people.length; i++) {
    peopleobject[i] = people[i]
}

// let's print the whole table
console.log(peopleobject)

// this is how firebase does it. it's a little more complicated, but it's much more efficient.

// the same for items

itemsobject = {}
for (var i = 0; i < items.length; i++) {
    itemsobject[i] = items[i]
}

// and for the purchase table object. let's try the object version first.

purchasecopyobjectobject = {
    0: { // note that we have to define the index ourselves. pretty good for databases. allows for custom ids.
        person: peopleobject[0],
        item: itemsobject[0]
    },
    1: {
        person: peopleobject[3],
        item: itemsobject[7]
    },
}

// let's print the whole table
console.log(purchasecopyobjectobject)

// what if hitagi changed her surname to hanekawa? let's try it. also hitagi belongs to hanekawa, not araragi lmaooooooo

peopleobject[0].last_name = "Hanekawa"

// let's print hitagi's purchase again
console.log(purchasecopyobjectobject[0])
// it still changes

// the index version should works the same.

// that was done under a javascript runtime, so it's easy, right?
// now, the problem. let's parse everything to JSON files.

// first, the arrays. for the sake of explanation, we'll put everything into the same object.

jsonarray = {
    people: people,
    items: items,
    purchasecopyobject: purchasecopyobject,
    purchaseindex: purchaseindex
}

jsonarraystring = JSON.stringify(jsonarray)


// and the objects

jsonobject = {
    people: peopleobject,
    items: itemsobject,
    purchasecopyobject: purchasecopyobjectobject,
}

jsonobjectstring = JSON.stringify(jsonobject)

// let's print the whole table

console.log(jsonarraystring)
console.log(jsonobjectstring)

// it's a string. we can't access the properties of the objects anymore. we can't even access the objects themselves. immortalized in a string.
// this means that if we changed hitagi's surname... again in the JSON file, it won't change in the purchase table.
// and last time i checked Firebase stores the table as a JSON file. so the whole "copy the object" thing will not work.



// so, how do we access the properties of the objects in the JSON file?
// we have to parse it back to an object.

// let's parse the array version first.

jsonarrayparsed = JSON.parse(jsonarraystring)

// or the respective functions in the respective languages. in python, it would be json.loads(peoplejson)
// now, let's screw up the table again.

jsonarrayparsed.people[0].first_name = "Madoka"
jsonarrayparsed.people[0].last_name = "Kaname"
jsonarrayparsed.items[0].name = "Kraber .50-Cal Sniper Rifle" // please do not use this in tf2
jsonarrayparsed.items[0].price = 99999.99
// let's print the whole table
console.log(jsonarrayparsed)

// or specifically, the first entry of the purchase table
console.log(jsonarrayparsed.purchasecopyobject[0]) // which is the first purchase, which is senjougahara buying bream, which should be madoka buying the kraber by now

// aaaaaand here's the problem. it doesn't change. because it's a copy of the object, not the object itself.
// this means you can't do the funny relational database thing where you change the name of the person and it changes in the purchase table too.
// if you want to do the foreign key trick, you have to either use the index version or write the code to change the name in the purchase table too.

// as for the index version
console.log(jsonarrayparsed.people[jsonarrayparsed.purchaseindex[0].person].first_name, jsonarrayparsed.items[jsonarrayparsed.purchaseindex[0].item].name)
// it works. but it's a little more complicated. but still, it works.

// now, the object version.

jsonobjectparsed = JSON.parse(jsonobjectstring)

jsonobjectparsed.people[0].first_name = "Madoka"
jsonobjectparsed.people[0].last_name = "Kaname"
jsonobjectparsed.items[0].name = "Kraber .50-Cal Sniper Rifle" // please do not use this in tf2
jsonobjectparsed.items[0].price = 99999.99

console.log(jsonobjectparsed.purchasecopyobject[0])
// it doesn't change. because it's a copy of the object, not the object itself.

// yup. JSON was not built for relational databases. it was built for storing data, not for storing relational tables.

// now, if it's not for RDB, why even use it?

// 1. it's easy to use. it's just a string. you can just copy and paste it into a text file and it will work. and it will work with any language.
// 2. firebase doesn't use SQL. it uses JSON. and it's the only reason why firebase is so popular.
// 3. it takes less space than SQL. and it's easier to read. and it's easier to write. and it's easier to parse. and it's easier to debug.
// 4. interoperability. it's easier to use with other languages. and it's easier to use with other databases. and it's easier to use with other programs.

// but when should you use SQL and when should you use JSON?
// if you're making a relational database, use SQL. if you're making a non-relational database, use JSON.
// if you're making a relational database, but you're too lazy to write SQL, use JSON. but you have to write the code to change the name in the purchase table too.

// Senjougahara buying Bread, which could be changed to Madoka buying Kraber anytime belongs to a relational database.
// Kafuka Fuura, Employee ID 123456, who is working on a new Assault Rifle with the research ID of 23489, belongs to the Research and Development Department, ran by Nozomu Itoshiki, Employee ID 789465, belongs to a relational database. ps. try writing an ER diagram for this.
// Alex Mason's data on a website, which updates everytime by referencing Alex Mason object again, belongs to a non-relational database.
// A certain website that store a certain selection of mangas, codenamed "November Hotel Echo November Tango Alpha India" stores the mangas as a JSON file. belongs to a non-relational database.

// And that's it. JSON vs SQL.
// All choices are valid. Except ZODB. like bro wtf is persistent.
// also MongoDB too. it's just JSON but with a different name. and it's not even a database. it's a database management system. it's just a glorified JSON file.
// especially pickle. DO NOT USE PICKLE. and if you do enjoy arbitrary code execution.

// postscript: any more NoSQL and plain not an SQL at all?
// Apache Cassandra: NoSQL by Facebook, now owned by Apache. Wide-column database. Used by Discord. Now you're tempted to use it.
// Redis: Hyper fast key-value database. Used by Twitter for caching.
// Neo4j: Graph database for... you guess it! Java!
// MongoDB and Firebase also have document databases. but they're just JSON but with a different name.

// what about prisma? Prisma is a database toolkit. it's not a database.
// but i saw it in an anime! that's prisma illya. not even a computing concept.