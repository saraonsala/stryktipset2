import csv
import io   
import urllib.request
from getPoisson import *
from game import *
from matchResult import *
import statistics



class Competition:
        def __init__(self, url):
                self.games = []
                self.teamNames =[]
                self.loadMatches(url)

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
                webpage = urllib.request.urlopen(url)
                datareader = csv.reader(io.TextIOWrapper(webpage))

                for row in datareader:
                        if row[6].isnumeric(): 
                                if len(self.games) > 20:
                                        game = Game(row[3],row[4],int(row[5]),int(row[6]), self.calculateAttackStrengthOfHomeTeam(row[3]), self.calculateAttackStrengthOfAwayTeam(row[4]))
                                else:
                                        game = Game(row[3],row[4],int(row[5]),int(row[6]), 1, 1)

                                self.games.append(game)
                                if row[3] not in self.teamNames:
                                        self.teamNames.append(row[3])
                #print("Listan med lag innehåller ",len(self.teamNames), "lag")
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
               
               
              

        def getAllResultsOLD(self, hTeamStrength, aTeamStrength):
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
              #  print("------------------------------")
              #  print("1X2 --------------------------")
              #  print("------------------------------")

                print("1:", "{:.2%}".format(homeProb), "X:", "{:.2%}".format(drawProb), " 2:","{:.2%}".format(awayProb))
              #  print("------------------------------")
              #  print("Troligt resultat -------------")
              #  print("------------------------------")
              #  for outcome in range(0,5):
              #          print(newList[outcome].result, "-", "{:.2%}".format(newList[outcome].probability))
              #  print("------------------------------")
              #  print("------------------------------")

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
                        return 1

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
                        return 1

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
                        return 1


        def getAverageGoalsByAllHomeTeams(self):
                #Hur många mål görs i snitt av hemmalagen?
                i = 0
                intGames = 0
                for team in self.games:
                        i+=team.homeGoals
                        intGames+=1
                try:
                        return i/intGames
                except ZeroDivisionError:
                        return 1

        def getAverageGoalsConcededByAllAwayTeams(self):
                return self.getAverageGoalsByAllHomeTeams()

        def getAverageGoalsConcededByAllHomeTeams(self):
                i = 0
                intGames = 0
                for game in self.games:
                        i+=game.awayGoals
                        intGames+=1
                try:
                        return i/intGames
                except ZeroDivisionError:
                        return 1


        def getAverageGoalsByAllAwayTeams(self):
                return self.getAverageGoalsConcededByAllHomeTeams()






        def calculateAttackStrengthOfHomeTeam(self, nameHomeTeam):
                #Vad har hemmalaget för offensiv styrka
                #Hur många mål gör laget på hemmaplan i förhållande till de andra lagen
                return (self.getAverageGoalsByHomeTeam(nameHomeTeam)/self.getAverageGoalsByAllHomeTeams())

        def calculateDefensiveStrengthOfHomeTeam(self, nameHomeTeam):
                #Vad har hemmalaget för defensiv styrka
                #Hur många mål släpper din in på hemmaplan i förhållande till de andra lagen
                return (self.getAverageGoalsConcededByHomeTeam(nameHomeTeam)/self.getAverageGoalsConcededByAllHomeTeams())


        def calculateAttackStrengthOfAwayTeam(self, nameAwayTeam):
                #Vad har hemmalaget för offensiv styrka
                #Hur många mål gör laget på bortaplan i förhållande till de andra lagen
                return  (self.getAverageGoalsByAwayTeam(nameAwayTeam)/self.getAverageGoalsByAllAwayTeams()) 

        def calculateDefensiveStrengthOfAwayTeam(self, nameAwayTeam):
                #Vad har bortalaget för defensiv styrka
                #Hur många mål släpper din in på hemmaplan i förhållande till de andra lagen
                return  (self.getAverageGoalsConcededByAwayTeam(nameAwayTeam)/self.getAverageGoalsConcededByAllAwayTeams()) 

        def calculateHomeTeamGoalExpectancy(self, strNameHomeTeam, strNameAwayTeam):
                #Home Team Goal Expectancy: Home attacking strength (1.20) x away defensive strength (1.07) x average goals home (1.57) = 2.02
                return self.calculateAttackStrengthOfHomeTeam(strNameHomeTeam) * self.calculateDefensiveStrengthOfAwayTeam(strNameAwayTeam) * self.getAverageGoalsByAllHomeTeams()

        def calculateAwayTeamGoalExpectancy(self, strNameHomeTeam, strNameAwayTeam):
                #Away Team Goal Expectancy: Away attacking strength (1.16) x home defensive strength (0.48) x average goals away (0.96) = 0.53
                return self.calculateAttackStrengthOfAwayTeam(strNameAwayTeam) * self.calculateDefensiveStrengthOfHomeTeam(strNameHomeTeam) * self.getAverageGoalsByAllAwayTeams()
 
        def calculateExpectedOutcome(self, nameHomeTeam, nameAwayTeam):         
                
                #BEHÖVS DENNA??????!
                #print(nameHomeTeam+' - '+ nameAwayTeam)
                
                strResult = self.getAllResults(nameHomeTeam, nameAwayTeam)
                #print(strResult)
                return strResult
