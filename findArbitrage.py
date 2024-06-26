import requests
import json
# docs url
# https://the-odds-api.com/liveapi/guides/v4/#parameters

api_key = 'YOUR-APIKEY-HERE'

getSportsEndpoint = 'https://api.the-odds-api.com/v4/sports/?apiKey=d63a10a144943fc29fe1f10d52677d07'
getSportsResponse = requests.get(getSportsEndpoint)
getSportsResponseData = getSportsResponse.json()

bookList = [
            "DraftKings",
            "FanDuel",
            "WynnBET",
            "PointsBet (US)",
            "MyBookie.ag",
            "BetMGM",
            "LowVig.ag",
            "BetOnline.ag",
            "Unibet",
            "BetRivers",
            "Caesars",
            "Bovada",
            "BetUS",
            "SuperBook",
            ]

def getSports(data):
    usableSports = []
    for sport in data:
        if (sport.get('has_outrights') == False): 
            usableSports.append(sport)
    
    return usableSports

def getOdds(odds):
    payload = ""
    
    if (odds < 2): 
            tmp = (100 / (odds-1)) *-1
            payload = str(tmp) 
    elif (odds == 2): 
        payload = "+100"
    else: 
        tmp = (odds-1) *100
        payload = "+" + str(tmp)

    return payload


def findArbitrage(teamPrice, team, teamIndex, bookList, currentBook, tmpDict):
    
    arbitrageodds = 0
    for targetBook in bookList:
        if (targetBook not in bookList): continue

        else:
            comparePrice = tmpDict[targetBook][teamIndex]["price"]
            compareTeam = tmpDict[targetBook][teamIndex]["name"]

            arbitrageodds = (1 / teamPrice ) + (1 / comparePrice)

            if (arbitrageodds < 1 and arbitrageodds > .6):
                if (teamIndex == 1): 
                    print(currentBook + ": " + str(teamPrice) + "(" + getOdds(teamPrice) + ")" + " + (" + team + ")")
                    print(targetBook + ": " + str(comparePrice) + "(" + getOdds(comparePrice) + ")" + " + (" + compareTeam + ")")
                else: 
                    print(targetBook + ": " + str(comparePrice) + "(" + getOdds(comparePrice) + ")" + " + (" + compareTeam + ")")
                    print(currentBook + ": " + str(teamPrice) + "(" + getOdds(teamPrice) + ")" + " + (" + team + ")")

                print(arbitrageodds)
                print('\n')

sportsList = getSports(getSportsResponseData)

for sportDict in sportsList:
    sport = sportDict.get('key')
    userInput = input(f'hit y to view {sport} results or any other key to continue: ')

    if (userInput != 'y'): continue
    else: 
        print(f'==={sport}===\n')
        main_endpoint = f'https://api.the-odds-api.com/v4/sports/{sport}/odds/?apiKey={api_key}&markets=h2h,spreads,totals&regions=us'

        response = requests.get(main_endpoint)
    
        if response.status_code == 200:

            response_content = response.text

            parsedResponse = json.loads(response_content)
            length = len(parsedResponse)
            tmpKey = parsedResponse[0]

            bookmakers = []
            games = []
            
            for i in range (length):
                game = parsedResponse[i]
                bigDict = {}

                if "bookmakers" in game:
                    bookmakers = game["bookmakers"]

                    for sportsbook in bookmakers:
                        tmpBook = sportsbook["title"]

                        if "markets" in sportsbook:
                            h2hGames = sportsbook["markets"][0]["outcomes"]
                            bigDict[tmpBook] = h2hGames

                        else: print("fail")

                    games.append(bigDict)
                    # printable = json.dumps(bigDict, indent=2)
                    
                else: 
                    print("something went wrong")
                
            highestHomeOdds = 0
            highestAwayOdds = 0

            winningHomeTeamBook = ""
            winningAwayteamBook = ""
            
            homeTeam = ""
            awayTeam = ""
            for i in range(len(games)):
                print('==New Game==')
                
                tmpDict = games[i]
                    
                for targetBook in bookList:
                    try:
                        # print(tmpDict[targetBook][0])
                        currentBook = targetBook
                        if (targetBook not in bookList): continue
                        else:
                            homeTeamPrice = tmpDict[targetBook][0]["price"]
                            awayTeamPrice = tmpDict[targetBook][1]["price"]
                            homeTeam = tmpDict[targetBook][0]["name"]
                            awayTeam = tmpDict[targetBook][1]["name"]

                            findArbitrage(homeTeamPrice, homeTeam, 1, bookList, currentBook, tmpDict)
                            
                    except KeyError:
                        continue
                        
        else:
            print(f"Error: {response.status_code} - {response.text}")
