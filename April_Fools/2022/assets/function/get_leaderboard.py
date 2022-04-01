from firebase_admin import db

def getLeaderboard():
    database = db.reference().get()
    usernameList = list(database.keys())
    timeList = []
    for username in usernameList:
        time = db.reference(f"{username}/time").get()
        timeList.append(time)
    username_timeDict = dict(zip(usernameList, timeList))
    leaderboard = [entry for entry in sorted(username_timeDict.items(), key=lambda entry: entry[1]) if entry[1] != 999999999 and entry[1] != 0]
    for i in range(len(leaderboard)):
        leaderboard[i] = (leaderboard[i][0], leaderboard[i][1])
    return leaderboard