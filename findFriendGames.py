import urllib.request;
import json;

apiKey = "8994027C0B161154DB8F7B72E6C57E80"

def getAPIKey():
    with open("apiKey") as f:
        return f.readline().replace('\n', "")

def getUserGames(userID):
    requestString = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={}&steamid={}&format=json".format(getAPIKey(), userID);
    
    lines = urllib.request.urlopen(requestString) 
    result = ""
    for line in lines:
        result += line.decode("utf-8");

    return result



def getUserGameList(userID):
    gameString = getUserGames(userID)

    data = json.loads(gameString)

    gameList = data["response"]["games"];

    result = []
    for game in gameList:
        result.append(game["appid"])

    return result

def getCommonGames(userList):
    commonGames = {}
    
    for user in userList:
        userGames = getUserGameList(user)


        for game in userGames:
            if not game in commonGames:
                commonGames[game] = 0
            
            commonGames[game] += 1

    result = []
    for game in commonGames:
        if commonGames[game] == len(userList):
            result.append(game)

    return result

user1 = "76561197996901884"
user2 = "76561198016701707"

#getUserGamesJson(userID);
print(getCommonGames([user1, user2, "76561198014865373", "76561198010718921"]))
