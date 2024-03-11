import csv
import io   
import urllib.request
from getPoisson import *
from game import *
from matchResult import *
import statistics
import pdb



class Competition:
        def __init__(self, url):
                self.games = []
                self.teamNames =[]
                self.numberOfMatches = 0
                self.averageNumberOfHomeGoals = 0
                self.averageNumberOfAwayGoals = 0
                self.numberOfHomeGoals = 0
                self.numberOfAwayGoals = 0
                self.loadMatches(url)

        def printGames(self):
                for i, game in enumerate(self.games, start=1):
                        print(f"Match {i}: {game.homeTeam} vs {game.awayTeam}, Resultat: {game.homeGoals}-{game.awayGoals}")
        
        def clearMatches(self):
                self.games = []
                self.numberOfMatches = 0
                self.averageNumberOfHomeGoals = 0
                self.averageNumberOfAwayGoals = 0
                self.teamNames = []

        def getTeamPoints(self, strTeamName):
                # för testsyfte för att kolla att allt fungerar.
                #returnerar poäng för laget
                intPoints = 0
                for game in self.games:
                        if game.homeTeam == strTeamName:
                                if game.homeGoals > game.awayGoals:
                                        intPoints+=3
                                if game.homeGoals == game.awayGoals:
                                        intPoints+=1
                        if game.awayTeam == strTeamName:
                                if game.homeGoals < game.awayGoals:
                                        intPoints+=3
                                if game.homeGoals == game.awayGoals:
                                        intPoints+=1
                return intPoints


        def loadMatches(self, url):
                #self.clearMatches()  # Rensa minnet innan nya matcher läses in
                #pdb.set_trace()
                webpage = urllib.request.urlopen(url)
                datareader = csv.reader(io.TextIOWrapper(webpage))

                for row in datareader:
                    if row[6].isnumeric(): 
                        if len(self.games) > 100:
                                game = Game(row[3], row[4], int(row[5]), int(row[6]), self.calculateAttackStrengthOfHomeTeam(row[3]), self.calculateAttackStrengthOfAwayTeam(row[4]))
                        else:
                                game = Game(row[3], row[4], int(row[5]), int(row[6]), 1, 1)

                        self.games.append(game)
                        self.numberOfMatches += 1
                        self.numberOfHomeGoals += game.homeGoals
                        self.numberOfAwayGoals += game.awayGoals
                        if row[3] not in self.teamNames:
                                self.teamNames.append(row[3])

                self.averageNumberOfHomeGoals = self.numberOfHomeGoals / self.numberOfMatches
                self.averageNumberOfAwayGoals = self.numberOfAwayGoals / self.numberOfMatches
                
                self.teamNames.sort()

        def showTeams(self):
                for name in self.teamNames:
                        print("[",self.teamNames.index(name)+1, "] ", name)

        def isTeamInCompetition(self, strTeamName):
                #Är laget med i denna liga?
                try:
                        if self.teamNames.index (strTeamName) >= 0:
                                return True
                        else:
                                return False
                except ValueError:
                        return False
                
                

        def get1X2(self, hTeamStrength, aTeamStrength):
                # Printar 1 x 2 i %'
                homeProb = 0
                awayProb = 0
                drawProb = 0
                results = []
                for x in range (0,10):
                        for y in range(0,10):           
                                result = MatchResult(str(x)+"-"+str(y),getPoisson(hTeamStrength,x,1)*getPoisson(aTeamStrength,y,1))
                                results.append(result)
                                if x > y:
                                        homeProb += result.probability
                                if y > x:
                                        awayProb += result.probability
                                if y==x:
                                        drawProb += result.probability

                newList = sorted(results,key=lambda result: result.probability)
                newList.reverse()
                
                print("1:", "{:.2%}".format(homeProb), "X:", "{:.2%}".format(drawProb), " 2:","{:.2%}".format(awayProb))
                print("------------------------------")
             
        def getAllResults(self, couponRow):
                # Uppdaterad version där vi skickar in en kupongrad för att att få ut de specifika värdena för 1 X 2
                # 2023-04-15
                
                homeProb = 0
                awayProb = 0
                drawProb = 0
                results = []
                for x in range (0,10):
                        for y in range(0,10):           
                                result = MatchResult(str(x)+"-"+str(y),getPoisson(self.calculateHomeTeamGoalExpectancy(couponRow.homeTeam, couponRow.awayTeam),x,1) * getPoisson(self.calculateAwayTeamGoalExpectancy(couponRow.homeTeam, couponRow.awayTeam),y,1))
                                results.append(result)
                                if x > y:
                                        homeProb += result.probability
                                elif y > x:
                                        awayProb += result.probability
                                else:
                                        drawProb += result.probability

                couponRow.homeProb ="{:.2%}".format(homeProb)
                couponRow.drawProb= "{:.2%}".format(drawProb)
                couponRow.awayProb= "{:.2%}".format(awayProb)
               
               
              

        

        def getTotalMadeGoals(self, specificTeam):
                i = 0
                intGames = 0
                for team in self.games:
                        #print(team.homeTeam)
                        if team.homeTeam == specificTeam:                               
                                i+=team.homeGoals
                        if team.awayTeam == specificTeam:
                                i+=team.awayGoals
                try:
                        return i/intGames
                except ZeroDivisionError:
                        return 1

        def getAverageGoalsByAwayTeam(self, specificTeam):
                i = 0
                intGames = 0
                for team in self.games:
                        if team.awayTeam == specificTeam:
                                i+=team.awayGoals
                                intGames+=1
                try:
                        return i/intGames
                except ZeroDivisionError:
                        return 1

        def getAverageGoalsConcededByAwayTeam(self, specificTeam):
                i = 0
                intGames = 0
                for team in self.games:
                        if team.awayTeam == specificTeam:
                                i+=team.homeGoals
                                intGames+=1
                try:
                        return i/intGames
                except ZeroDivisionError:
                        return 0

        def getAverageGoalsByHomeTeam(self, specificTeam):
                i = 0
                intGames = 0
                for team in self.games:
                        if team.homeTeam == specificTeam:
                                i+=team.homeGoals
                                intGames+=1
                try:
                        return i/intGames
                except ZeroDivisionError:
                        return 0

        def getAverageGoalsConcededByHomeTeam(self, specificTeam):
                i = 0
                intGames = 0
                for team in self.games:
                        if team.homeTeam == specificTeam:
                                i+=team.awayGoals
                                intGames+=1
                try:
                        return i/intGames
                except ZeroDivisionError:
                        return 0


        def getAverageGoalsByAllHomeTeams(self):
                #Hur många mål görs i snitt av hemmalagen?
                try:
                        return self.averageNumberOfHomeGoals
                except ZeroDivisionError:
                        return 0

        def getAverageGoalsConcededByAllAwayTeams(self):
                try:
                        return self.averageNumberOfHomeGoals
                except ZeroDivisionError:
                        return 0

        def getAverageGoalsConcededByAllHomeTeams(self):
                try:
                        return self.averageNumberOfAwayGoals
                except ZeroDivisionError:
                        return 0

        def getAverageGoalsByAllAwayTeams(self):
                try:
                        return self.averageNumberOfAwayGoals
                except ZeroDivisionError:
                        return 0






        def calculateAttackStrengthOfHomeTeam(self, nameHomeTeam):
                #Vad har hemmalaget för offensiv styrka
                #Hur många mål gör laget på hemmaplan i förhållande till de andra lagen
                try:
                        return (self.getAverageGoalsByHomeTeam(nameHomeTeam)/self.getAverageGoalsByAllHomeTeams())
                except ZeroDivisionError:
                        return 0

        def calculateDefensiveStrengthOfHomeTeam(self, nameHomeTeam):
                #Vad har hemmalaget för defensiv styrka
                #Hur många mål släpper din in på hemmaplan i förhållande till de andra lagen
                try: 
                        return (self.getAverageGoalsConcededByHomeTeam(nameHomeTeam)/self.getAverageGoalsConcededByAllHomeTeams())
                except ZeroDivisionError:
                        return 0
        

        def calculateAttackStrengthOfAwayTeam(self, nameAwayTeam):
                #Vad har hemmalaget för offensiv styrka
                #Hur många mål gör laget på bortaplan i förhållande till de andra lagen
                try: 
                        return  (self.getAverageGoalsByAwayTeam(nameAwayTeam)/self.getAverageGoalsByAllAwayTeams()) 
                except ZeroDivisionError:
                        return 0

        def calculateDefensiveStrengthOfAwayTeam(self, nameAwayTeam):
                #Vad har bortalaget för defensiv styrka
                #Hur många mål släpper din in på hemmaplan i förhållande till de andra lagen
                try: 
                        return  (self.getAverageGoalsConcededByAwayTeam(nameAwayTeam)/self.getAverageGoalsConcededByAllAwayTeams()) 
                except ZeroDivisionError:
                        return 0
                
        def calculateHomeTeamGoalExpectancy(self, strNameHomeTeam, strNameAwayTeam):
                #Home Team Goal Expectancy: Home attacking strength (1.20) x away defensive strength (1.07) x average goals home (1.57) = 2.02
                try:
                        return self.calculateAttackStrengthOfHomeTeam(strNameHomeTeam) * self.calculateDefensiveStrengthOfAwayTeam(strNameAwayTeam) * self.getAverageGoalsByAllHomeTeams()
                except ZeroDivisionError: 
                        return 0
                

        def calculateAwayTeamGoalExpectancy(self, strNameHomeTeam, strNameAwayTeam):
                #Away Team Goal Expectancy: Away attacking strength (1.16) x home defensive strength (0.48) x average goals away (0.96) = 0.53
                try:
                        return self.calculateAttackStrengthOfAwayTeam(strNameAwayTeam) * self.calculateDefensiveStrengthOfHomeTeam(strNameHomeTeam) * self.getAverageGoalsByAllAwayTeams()
                except ZeroDivisionError:
                        return 0
                

