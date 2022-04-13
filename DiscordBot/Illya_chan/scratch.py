# usin = input()

# operandIndex = []
# previousOperandIndex = 0
# operandCount = 0
# for i in range(len(usin)):
#     if usin[i] == '+' or usin[i] == '-':
#         operandIndex.append(list())
#         operandIndex[operandCount].append(previousOperandIndex)
#         operandIndex[operandCount].append(i)
#         previousOperandIndex = i
#         operandCount += 1

# termList = []
# for i in range(len(operandIndex)):
#     termList.append(usin[operandIndex[i][0]:operandIndex[i][1]])
# try:
#     termList.append(usin[operandIndex[len(operandIndex) - 1][1]:])
# except:
#     termList.append(usin)
#     termList.append("+0")
#     termList.append("+0")
# termList = termList[::-1]

# termListArranged = [0] * 256
# pos = 0
# for index, term in enumerate(termList):
#     if "x^" + str(index) in term:
#         try:
#             termListArranged[pos] = eval(term.replace("x^" + str(index), "")) * index
#         except:
#             termListArranged[pos] = eval(term.replace("x^" + str(index), "1")) * index
#         finally:
#             if eval(str(termListArranged[pos])) >= 0:
#                 termListArranged[pos] = "+" + str(termListArranged[pos])
#             termListArranged[pos] = str(termListArranged[pos]) + "x^" + str(index - 1)
#     elif "x^" + str(index + 1) in term:
#         try:
#             termListArranged[pos + 1] = eval(term.replace("x^" + str(index + 1), "")) * (index + 1)
#         except:
#             termListArranged[pos + 1] = eval(term.replace("x^" + str(index + 1), "1")) * (index + 1)
#         finally:
#             if eval(str(termListArranged[pos + 1])) >= 0:
#                 termListArranged[pos + 1] = "+" + str(termListArranged[pos + 1])
#             termListArranged[pos + 1] = str(termListArranged[pos + 1]) + "x^" + str(index)
#     elif "x" in term:
#         if term == "-x":
#             termListArranged[pos] = "-1"
#         elif term == "x":
#             termListArranged[pos] = "1"
#         else:
#             termListArranged[pos] = term.replace("x", "")
#     pos += 1

# termListArranged.pop(0)
# termListArranged = termListArranged[::-1]
# final = (''.join([term for term in termListArranged if term != 0])).replace("^1", "")
# if final.startswith("+"):
#     final = final[1:]
# elif final.startswith("^"):
#     split = usin.split("x^")
#     final = f"{eval(split[1])}x^{eval(split[1]) - 1}"
# elif len(final) == 3:
#     split = usin.split("x^")
#     final = f"{eval(split[0]) * eval(split[1])}x^{eval(split[1]) - 1}"

# print(final)

# import openai
# openai.organization = "org-TJtqRXslGpBcNwXFXtWQTn8t"
# openai.api_key = "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"

# response = openai.Completion.create(
#     engine="text-davinci-002",
#     prompt="recommend me a place to travel",
#     temperature=0.7,
#     max_tokens=256,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
# )

# print(response["choices"][0]["text"])

# sort a list of list based on the first element of the list
# def sort_list(list_of_list):
#     return sorted(list_of_list, key=lambda x: x[0])








# def sort_dict(dict):
#     sorted_dict = sorted(dict.items(), key=lambda x: x[0], reverse=True)
#     new_dict = {}
#     for i in range(len(sorted_dict)):
#         new_dict[sorted_dict[i][0]] = sorted_dict[i][1]
#     return new_dict


# dict = {50: 0, 100: 1}
# print(sort_dict(dict))






# listtt = [0,20,40,60]

# for i in range(len(listtt) - 1):
#     if i == 1:
#         listtt.remove(60)
#     print(listtt[i])

# import turtle as t

# t.pen(pencolor="red", fillcolor="red", pensize=3)
# t.begin_fill()
# t.lt(50)
# t.fd(133)
# t.circle(50, 200)
# t.rt(140)
# t.circle(50, 200)
# t.fd(133)
# t.end_fill()

# t.done()





# def say(usin):
#     match usin:
#         case "nya":
#             print("You said nya!")
#         case "iku" | "nya":
#             print("You just coom ><")
#         case [action, time]:
#             print(f"I {action} at {time}")
#         case [('coom' | 'sleep' | 'eat') as action, time]:
#             print(f"I {action} at {time}")
#         case _:
#             print("I sleep")

# say("nya")  # You said nya!
# say("iku")  # You just coom ><
# say("nya")  # You said nya!
# say(["afternoon", "work"])  # I worked at afternoon
# say(["coom", "afternoon"])  # I coom at afternoon
# say("nani")  # I sleep

sum = 0
for i in range(21):
    if i % 2 != 0:
        sum += 2**i

print(sum)