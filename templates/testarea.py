from competition import *

urlPremierLeague = "https://www.football-data.co.uk/mmz4281/2223/E0.csv"
urlChampionship = "https://www.football-data.co.uk/mmz4281/2223/E1.csv"

premierLeague = Competition(urlPremierLeague)
championship = Competition(urlChampionship)

#LÄnk till formler etc https://www.sbo.net/strategy/football-prediction-model-poisson-distribution/



strHomeTeam = "Brighton"
strAwayTeam ="Liverpool"

print("Hemmamål snitt i ligan: " + str(premierLeague.getAverageGoalsByAllHomeTeams()))
print("Bortamål snitt i ligan: " + str(premierLeague.getAverageGoalsByAllAwayTeams()))
print("Innläppta mål av hemmalag, snitt i ligan: " + str(premierLeague.getAverageGoalsConcededByAllHomeTeams()))
print("Inläppta mål av bortalag, snitt i ligan: " + str(premierLeague.getAverageGoalsConcededByAllAwayTeams()))

print ("Hemmamål i snitt för "+ strHomeTeam +": "+  str(premierLeague.getAverageGoalsByHomeTeam(strHomeTeam)))
print ("Bortamål i snitt för " + strAwayTeam+": "+ str(premierLeague.getAverageGoalsByAwayTeam(strAwayTeam)))
print ("Insläppta mål på hemmaplan, i snitt: " + str(premierLeague.getAverageGoalsConcededByHomeTeam(strHomeTeam)))
print ("INsläppta mål på bortaplan, i snitt: " + str(premierLeague.getAverageGoalsConcededByAwayTeam(strAwayTeam)))

print("-----Expectectd Goals--------")
print("ExG: "+ strHomeTeam+ str(premierLeague.calculateHomeTeamGoalExpectancy(strHomeTeam, strAwayTeam)))
print("ExG: "+ strAwayTeam+ str(premierLeague.calculateAwayTeamGoalExpectancy(strHomeTeam, strAwayTeam)))

print ("poäng: " + str(premierLeague.getTeamPoints(strHomeTeam)))
