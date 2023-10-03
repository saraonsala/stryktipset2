import requests
from competition import *
from bs4 import BeautifulSoup

#urlPremierLeague = "https://www.football-data.co.uk/mmz4281/2223/E0.csv"
#urlChampionship = "https://www.football-data.co.uk/mmz4281/2223/E1.csv"

#premierLeague = Competition(urlPremierLeague)
#championship = Competition(urlChampionship)


def cleanTeamNames(strTeamName):
        #Undantagshantering för alla lag som har en avvikande stavning på sidan (se variabel strURL nedan)
        #som stryktipskupongen hämtas ifrån
        
        if strTeamName == 'Manchester City': 
                return 'Man City'
        elif strTeamName == 'Crystal Palace ':
                return 'Crystal Palace'
        elif strTeamName == 'Arsenal ':
                return 'Arsenal'
        elif strTeamName == 'Wolverhampton':
                return 'Wolves'
        elif strTeamName == 'Manchester United':
                return 'Man United'
        elif strTeamName == 'Queens Park Rangers':
                return 'QPR'
        elif strTeamName == 'Sheffield U':
                return 'Sheffield United'
        elif strTeamName == 'Nottingham Forest':
                return "Nott'm Forest"
        elif strTeamName == 'Blackburn Rovers':
                return "Blackburn"
        elif strTeamName == 'West Bromwich':
                return "West Brom"
        elif strTeamName == 'Charlton':
                return "Charlton"
        else: return strTeamName

def getNext13Games(thisCoupon, premierLeague, championship):
        #Webscraping, plockar ut nästa veckas stryktipsmatcher
        strUrl = 'https://tipsrader.se/'
        hometeams=[]
        awayteams=[]
        response = requests.get(strUrl)
        soup = BeautifulSoup(response.text, 'html.parser')
        for tag in soup.find_all(class_='hometeam hide-for-small-only'):
                hometeams.append(cleanTeamNames(tag.text))
        for tag in soup.find_all(class_='awayteam hide-for-small-only'):
                awayteams.append(cleanTeamNames(tag.text))         
        for i in range(13):
                if premierLeague.isTeamInCompetition(awayteams[i]):
                        thisCoupon.addCouponRow(hometeams[i], awayteams[i])
                elif championship.isTeamInCompetition(awayteams[i]):
                        thisCoupon.addCouponRow(hometeams[i], awayteams[i])
                else:
                        print(":"+awayteams[i] + ":. Kunde inte hitta bortalaget. Troligtvis felstavat eller i en annan liga  ")               
                
        
                        



        