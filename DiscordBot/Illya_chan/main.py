import discord
import random
import re
import math
import numpy
import urllib
import json
from forex_python.converter import CurrencyRates
from keep_alive import keep_alive

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
                  f"{str(message.author.mention)} daisuki!",
                  f"Eh heh heh. I like it when {str(message.author.mention)} pat me on the head, {str(message.author.mention)}…" +
                  "Ah, if you could help me dry and brush my hair next time… Eh!? We can't take a bath together!!! …Yet…",
                  "I'm not afraid. No matter how strong the enemies are, or what fate lies in store for us, I know " +
                  f"that you'll be even stronger, {str(message.author.mention)}. I believe in you!"]
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
    help_dict = {"nh": "> Search for specific doujin: `./nh <number>`\n> Search for random doujin: `./nh`\n\nExample:\n`./nh 208208`\n`./nh`",
                 "calc": "> Perform calculations: `./calc <expression>`\n\nExample:\n`./calc 5+2(11/128)`\n`./calc (sin(pi/2) + cos(e/2)) + factorial(5)`\n\n" +
                 "Supported functions and constants:\n`sin(x), cos(x), tan(x), asin(x), acos(x), atan(x),\nsqrt(x), cbrt(x), log(x, base), exp(x), abs(x),\nfloor(x), ceil(x), " +
                 "round(x), factorial(x), x % y, x mod y,\npi, e`",
                 "convert": "> Convert currencies: `./convert <amount> <from> <to>`\n\nExample:\n`./convert 100 EUR JPY`",
                 "help": "**Illya is here! What would you like to do, master~?**\n\n" +
                 "> Nya chatting\n" +
                 "`nya` (symbols/cases/repeating letters are acceptable)\n\n"
                 "> Search for doujin\n" +
                 "`./nh <number>`\n" +
                 "`./nh`\n\n" +
                 "> Perform calculations\n" +
                 "`./calc <expression>`\n\n" +
                 "> Convert currency\n" +
                 "`./convert <amount> <from> <to>`\n\n" +
                 "> Covid-19 statistics\n" +
                 "`./covid`\n\n" +
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
                await message.channel.send(f"{help_dict['help']}")
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
                                        f"New case (excluded foreigner): `{data['new_case_excludeabroad']:,}`\n" +
                                        f"Total case (excluded foreigner): `{data['total_case_excludeabroad']:,}`\n" +
                                        f"New death: `{data['new_death']:,}`\n" +
                                        f"Total death: `{data['total_death']:,}`\n" +
                                        f"New recovered: `{data['new_recovered']:,}`\n" +
                                        f"Total recovered: `{data['total_recovered']:,}`\n\n" +
                                        f"Source: https://covid19.ddc.moph.go.th/\n" +
                                        "Take care of yourself na ka 😔")
        return 0


keep_alive()

# Token, do not delete
client.run('ODQ1MzEyMjg4MDc2NTk1MjAw.YKfIag.xiv-cypSxRSvlXeRq2ccxwXcGkQ')
