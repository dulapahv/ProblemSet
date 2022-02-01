import discord
import random
import re
import math
import numpy
import urllib
import json
from firebase_admin import initialize_app, credentials, db
from forex_python.converter import CurrencyRates
from keep_alive import keep_alive

# Authenticate database
cred = credentials.Certificate(
    "DiscordBot\Illya_chan\illya-key.json")  # illya-key.json
initialize_app(cred, {
               "databaseURL": "https://illya-discord-bot-default-rtdb.asia-southeast1.firebasedatabase.app/"})

test = db.reference("test")
print(test.get())

client = discord.Client()


@client.event
async def on_ready():
    print("{0.user} is now online!".format(client))


###############################################
# Function that removes duplicate letter from a string
def remove_duplicate_letter(string):
    letter_list = []
    result = []
    for letter in string:
        if letter not in letter_list:
            letter_list.append(letter)
    for letter in letter_list:
        result.append(letter)
    return ''.join(result)


###############################################
@client.event
async def on_message(message):
    nya_input = ["nya"]
    nya_output = ["Nya! Gochujinsama",
                  "Hiya!",
                  "Mou~",
                  "Dame~",
                  "Fue?!",
                  "Nya!",
                  "Iku!",
                  f"{message.author.mention} daisuki!",
                  f"Eh heh heh. I like it when {message.author.mention} pat me on the head." +
                  "...Ah, if you could help me dry and brush my hair next time… Eh!? We can't take a bath together!!! …Yet…",
                  "I'm not afraid. No matter how strong the enemies are, or what fate lies in front of us, I know " +
                  f"that you'll be even stronger, {message.author.mention}. I believe in you!"]
    horny_goodluck = ["ehehe~ Goodluck na ka~",
                      "Don't forget to clean up na ka~",
                      "It's better to beat meat than to do meth!",
                      "Protect and have s*x!"]
    math_func = {"sin": "math.sin",
                 "cos": "math.cos",
                 "tan": "math.tan",
                 "asin": "math.asin",
                 "acos": "math.acos",
                 "atan": "math.atan",
                 "sqrt": "math.sqrt",
                 "cbrt": "numpy.cbrt",
                 "log": "math.log",
                 "exp": "math.exp",
                 "abs": "math.abs",
                 "floor": "math.floor",
                 "ceil": "math.ceil",
                 "round": "math.round",
                 "factorial": "math.factorial",
                 "pi": "math.pi",
                 "e": "math.e",
                 "mod": "%"}
    help_dict = {"nh": "> Search for specific doujin:\n`./nh <number>`\n\n> Search for random doujin:\n`./nh`\n\nExample:\n`./nh 208208`\n`./nh`",
                 "calc": "> Perform calculations: `./calc <expression>`\n\nExample:\n`./calc 5+(2*(11/128))`\n`./calc (sin(pi/2) + cos(e/2)) + factorial(5)`\n\n" +
                 "Supported functions and constants:\n`sin(x), cos(x), tan(x), asin(x), acos(x), atan(x),\nsqrt(x), cbrt(x), log(x, base), exp(x), abs(x),\nfloor(x), ceil(x), " +
                 "round(x), factorial(x), x % y, x mod y,\npi, e`",
                 "convert": "> Convert currencies: `./convert <amount> <from> <to>`\n\nExample:\n`./convert 100 EUR JPY`",
                 "event": "> Add event:\n`./event add <event name>;<event date>;<event time>;<event description>`\n\n" +
                 "> Delete event:\n`./event delete <event name>`\n\n" +
                 "> View event:\n`./event view`\n`./event view <event name>`\n\n" +
                 "> Update event:\n`./event update <event name>;<event date>;<event time>;<event description>`\n\n" +
                 "Example: \n`./event add Birthday;06-03-2022;00:00:00;n0miya's Birthday!`\n`./event delete Birthday`\n`./event view`\n`./event view Birthday`" +
                 "\n`./event update Birthday;22-08-2022;00:00:00;Nunoko's Birthday!`",
                 "help": "**Illya is here! What would you like to do, master~?**\n\n" +
                 "> Nya chatting\n" +
                 "`nya` (symbols/different cases/repeating letters are acceptable)\n\n"
                 "> Search for doujin\n" +
                 "`./nh <number>`\n" +
                 "`./nh`\n\n" +
                 "> Perform calculations\n" +
                 "`./calc <expression>`\n\n" +
                 "> Convert currency\n" +
                 "`./convert <amount> <from> <to>`\n\n" +
                 "> Covid-19 statistics\n" +
                 "`./covid`\n\n" +
                 "> Event\n" +
                 "`./event add <event name>;<event date>;<event time>;<event description>`\n" +
                 "`./event delete <event name>`\n" +
                 "`./event view`\n" +
                 "`./event view <event name>`\n" +
                 "`./event update <event name>;<event date>;<event time>;<event description>`\n\n" +
                 "> Get help\n" +
                 "`./help`\n" +
                 "`./?`\n" +
                 "`./help <command>`\n" +
                 "`./? <command>`"}

    # Prevent bot from responding to author's request
    if message.author == client.user:
        return

    # Respond to user's message
    if remove_duplicate_letter(re.sub('[^A-Za-z0-9]+', '', message.content.lower())) in nya_input:
        await message.channel.send(random.choice(nya_output))
        return 0

    # Respond to user's message
    if message.content.startswith("./nh"):
        usin = message.content.replace("./nh ", "")
        if usin == "./nh":
            await message.channel.send(f"{random.choice(horny_goodluck)}\nhttps://nhentai.net/random/")
        elif usin.isnumeric():
            await message.channel.send(f"{random.choice(horny_goodluck)}\nhttps://nhentai.net/g/{usin}")
        else:
            await message.channel.send(f"Invalid syntax na ka~\n\n{help_dict['nh']}")
        return 0

    # Perform calculations
    if message.content.startswith("./calc"):
        usin = message.content.replace("./calc ", "")
        if usin == "./calc":
            await message.channel.send(f"Invalid syntax na ka~\n\n{help_dict['calc']}")
        else:
            for key, value in math_func.items():
                usin = usin.replace(key, value)
            try:
                result = eval(usin)
            except Exception as error:
                await message.channel.send(f"Something is not right, master...😅\n\n`{error}`")
                return 0
            try:
                await message.channel.send(f"The answer is `{round(result, 3):,}`")
            except Exception as error:
                await message.channel.send(f"Something is not right, master...😅\n\n`{error}`")
                return 0

    # Convert currency
    if message.content.startswith("./convert"):
        usin = message.content.replace("./convert ", "")
        if usin == "./convert":
            await message.channel.send(f"Invalid syntax na ka~\n\n{help_dict['convert']}")
        else:
            try:
                usin = usin.split(" ")
                amount = float(usin[0])
                from_ = usin[1]
                to_ = usin[2]
                converter = CurrencyRates()
                result = converter.convert(from_, to_, amount)
                await message.channel.send(f"{amount:,} {from_} is {round(result, 2):,} {to_}")
            except Exception as error:
                await message.channel.send(f"Invalid syntax na ka~\n\n{help_dict['convert']}")
                return 0

    # Show help
    if message.content.startswith("./help") or message.content.startswith("./?"):
        usin = message.content.split(" ")
        try:
            usin[1] == ""
        except:
            await message.channel.send(f"{help_dict['help']}")
        else:
            try:
                await message.channel.send(help_dict[usin[1]])
            except:
                await message.channel.send(f"Help page not found. Type `./help` or `./?` to see all commands.")
        return 0

    # Display Covid information
    if message.content.startswith("./covid"):
        with urllib.request.urlopen("https://covid19.ddc.moph.go.th/api/Cases/today-cases-all") as url:
            data = url.read()
            data = data.decode("utf-8")
            data = data.replace("[", "").replace("]", "")
            data = json.loads(data)
            await message.channel.send(f"> Covid report on {data['update_date']}\n\n" +
                                       f"New case: `{data['new_case']:,}`\n" +
                                       f"Total case: `{data['total_case']:,}`\n" +
                                       f"New case (excluding foreigner): `{data['new_case_excludeabroad']:,}`\n" +
                                       f"Total case (excluding foreigner): `{data['total_case_excludeabroad']:,}`\n" +
                                       f"New death: `{data['new_death']:,}`\n" +
                                       f"Total death: `{data['total_death']:,}`\n" +
                                       f"New recovered: `{data['new_recovered']:,}`\n" +
                                       f"Total recovered: `{data['total_recovered']:,}`\n\n" +
                                       f"Source: https://covid19.ddc.moph.go.th/\n" +
                                       "Take care of yourself na ka 😔")
        return 0

    # Managing event
    if message.content.startswith("./event"):
        usin = message.content.replace("./event ", "")
        if usin == "./event":
            await message.channel.send(f"Invalid syntax na ka~\n\n{help_dict['event']}")
        else:
            try:
                if usin.startswith("add"):
                    usin = usin.replace("add ", "")
                    try:
                        name, date, time, desc = usin.split(";")
                    except:
                        await message.channel.send(f"Invalid syntax na ka~\n\n{help_dict['event']}")
                        return 0
                    event = db.reference(name)
                    event.set({
                        "name": name,
                        "date": date,
                        "time": time,
                        "desc": desc
                    })
                    await message.channel.send(f"Event `{name}` has been added!")

                elif usin.startswith("remove"):
                    usin = usin.replace("remove ", "")
                    try:
                        event = db.reference(usin)
                        event.delete()
                    except:
                        return 0
                    await message.channel.send(f"Event `{usin}` has been removed!")

                elif usin.startswith("view"):
                    usin = usin.replace("view ", "")
                    event = db.reference().get()
                    if usin == "view":
                        for name in event.keys():
                            await message.channel.send(f"```Name: {event[name]['name']}\n" +
                                                       f"Date: {event[name]['date']}\n" +
                                                       f"Time: {event[name]['time']}\n" +
                                                       f"Description: {event[name]['desc']}```")
                    else:
                        await message.channel.send(f"```Name: {event[usin]['name']}\n" +
                                                   f"Date: {event[usin]['date']}\n" +
                                                   f"Time: {event[usin]['time']}\n" +
                                                   f"Description: {event[usin]['desc']}```")

                elif usin.startswith("update"):
                    usin = usin.replace("update ", "")
                    try:
                        name, date, time, desc = usin.split(";")
                    except:
                        await message.channel.send(f"Invalid syntax na ka~\n\n{help_dict['event']}")
                        return 0
                    event = db.reference(name)
                    event.update({
                        "name": name,
                        "date": date,
                        "time": time,
                        "desc": desc
                    })
                    await message.channel.send(f"Event `{name}` has been updated!")
                else:
                    await message.channel.send(f"Invalid syntax na ka~\n\n{help_dict['event']}")
            except Exception as error:
                await message.channel.send(f"Something is not right, master...😅\n\n`{error}`\n\nType `./help event` or `./? event` to get help.")
        return 0


keep_alive()

# Token, do not delete
client.run('ODQ1MzEyMjg4MDc2NTk1MjAw.YKfIag.wgCWgKjOGJ5QFk_3zy_S4vF1aTk')
