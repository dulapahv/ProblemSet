import discord
import random
from keep_alive import keep_alive

client = discord.Client()


@client.event
async def on_ready():
    print("Nyaaaaa {0.user}".format(client))


@client.event
async def on_message(message):
    nya_input = ["./Nya", "./nya", "./nyaa", "./Nyaa", "./Nya!", "./Nyaa!", "./nya!", "./nyaa!", "./Nyaaa", "./Nyaaa!",
                 "./nyaaa", "./nyaaa!"]
    nya_output = ["Nya! Gochujinsama", "Hiya!", "Mou~", "Dame~", "Fue?!", "Nya!", "Iku!", str(message.author.mention) +
                  " daisuki!",
                  "Eh heh heh. I like it when " + str(message.author.mention) + " pat me on the head, " +
                  str(message.author.mention) + "… Ah, if you could help me dry and brush my hair next time… Eh!? We "
                                                "can’t take a bath together!!! …Yet…",
                  "I’m not afraid. No matter how strong the enemies are, or what fate lies in store for us, I know "
                  "that you’ll be even stronger, " + str(message.author.mention) + ". I believe in you!"]
    tu_input = ["tu", "Tu", "Tu", "Prayut", "prayut", "prawit", "Prawit", "โอ้ก", "พระบาทสมเด็จเหี้ยโอ", "ไอเหี้ยโอ"]
    tu_output = ["kuay", "hee", "go die"]
    unacceptables = [" "]

    # Prevent bot from responding to author's request
    if message.author == client.user:
        return

    # Check for nya input
    if any(word in message.content for word in nya_input) and not any(word in message.content for word in unacceptables):
        await message.channel.send(random.choice(nya_output))

    # Check for nh code, if there is no code then random
    if message.content.startswith("./nh"):
        if message.content != "./nh":
            if len(message.content) == 10:
                await message.channel.send('https://nhentai.net/g/' + message.content[4] + message.content[5] +
                                           message.content[6] + message.content[7] + message.content[8] +
                                           message.content[9])
            elif len(message.content) == 9:
                await message.channel.send('https://nhentai.net/g/' + message.content[4] + message.content[5] +
                                           message.content[6] + message.content[7] + message.content[8])
            elif len(message.content) == 8:
                await message.channel.send('https://nhentai.net/g/' + message.content[4] + message.content[5] +
                                           message.content[6] + message.content[7])
            elif len(message.content) == 7:
                await message.channel.send('https://nhentai.net/g/' + message.content[4] + message.content[5] +
                                           message.content[6])
            elif len(message.content) == 6:
                await message.channel.send('https://nhentai.net/g/' + message.content[4] + message.content[5])
            elif len(message.content) == 5:
                await message.channel.send('https://nhentai.net/g/' + message.content[4])
    if message.content == "./nh":
        nuclear = random.randint(1, 360509)
        await message.channel.send("https://nhentai.net/g/" + str(nuclear))
      
    if message.content == "ror10":
        await message.channel.send("kuay")

    if any(word in message.content for word in tu_input):
        await message.channel.send(random.choice(tu_output))

keep_alive()

# if any(word in message.content for word in nya_input):

# Token, do not delete
client.run('ODQ1MzEyMjg4MDc2NTk1MjAw.YKfIag.xiv-cypSxRSvlXeRq2ccxwXcGkQ')

'''
    if message.content.startswith("horny"):
        nhentai = NHentai()
        random_doujin = nhentai.get_random()
        await message.channel.send(random_doujin)
    '''

'''
   if message.content.startswith("nya"):
       await message.channel.send("nya! gochujinsama!")
   '''


# import discord
# import random
# from keep_alive import keep_alive

# client = discord.Client()

# @client.event
# async def on_ready():
#     print("Illya-chan is now ready to help!")

# removeChar = ["!", ".", ","]

# # Greetings
# greetingsList = ["Hi master~",
#                  "Hi master, how are you today?",
#                  "I'm quite sleepy today~"]
# greetingsTrig = ["hi illya",
#                  "good morning illya",
#                  "good afternoon illya",
#                  "good evening illya"]

# # Sweet Talk
# sweetTalkList = ["Nya~",
#                  "Nya nya~",
#                  "Eh heh heh~ It tickles"]

# # Life Coach



# @client.event
# async def on_message(message):
#   # Prevent bot from responding to author's request
#   if message.author == client.user:
#     return

#   try:

#     msg = message.content.lower()
#     # msg = ''.join(sorted(set(msg), key=msg.index))
#     msg = msg.replace(*removeChar, "")
#     print(msg)

  
#     if msg in greetingsTrig:
#       await message.channel.send(random.choice(greetingsList))

#   except Exception as error:
#     await message.channel.send(f"I-I don't feel well, master... {error}")
    


# keep_alive()

# # if any(word in message.content for word in nya_input):

# # Token, do not delete
# client.run('ODQ1MzEyMjg4MDc2NTk1MjAw.YKfIag.xiv-cypSxRSvlXeRq2ccxwXcGkQ')

# '''
#     if message.content.startswith("horny"):
#         nhentai = NHentai()
#         random_doujin = nhentai.get_random()
#         await message.channel.send(random_doujin)
#     '''

# '''
#    if message.content.startswith("nya"):
#        await message.channel.send("nya! gochujinsama!")
#    '''
