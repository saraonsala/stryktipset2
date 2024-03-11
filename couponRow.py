from competition import *

class CouponRow:
        def __init__(self, homeTeam, awayTeam, numberofRowsinArray):
            #Initierar en kupongrad 
            self.matchnumber = numberofRowsinArray +1
            self.homeTeam = homeTeam
            self.awayTeam = awayTeam
            self.homeProbOrder = 0
            self.drawProbOrder = 0
            self.awayProbOrder = 0
            self.homeProb = 0
            self.drawProb = 0
            self.awayProb = 0
            self.one =""
            self.two =""
            self.ex =""
            self.combined = ""


