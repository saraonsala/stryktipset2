from webscraping import *
from competition import *

print("Startar Pelles fotbollsprogram 1.5 - Single Game mode...")

#URL:er till csv-filer online
#URL:er till csv-filer online
urlPremierLeague = "https://www.football-data.co.uk/mmz4281/2223/E0.csv"
urlChampionship = "https://www.football-data.co.uk/mmz4281/2223/E1.csv"

premierLeague = Competition(urlPremierLeague)
championship = Competition(urlChampionship)

premierLeague.chooseTeams()

#a = "1-2"
#print(a[a.find('-')+1:len(a)])

