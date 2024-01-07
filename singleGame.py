from webscraping import *
from competition import *

#URL:er till csv-filer online
urlPremierLeague = "https://www.football-data.co.uk/mmz4281/2223/E0.csv"
urlChampionship = "https://www.football-data.co.uk/mmz4281/2223/E1.csv"

premierLeague = Competition(urlPremierLeague)
championship = Competition(urlChampionship)

premierLeague.chooseTeams()



