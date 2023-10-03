from couponRow import *
import operator

class Coupon:
        def __init__(self):
                #Initierar en kupong som på det hela taget bara innehåller en array med rader.
                self.couponrows = []


        def addCouponRow(self, homeTeam, awayTeam):
                newCouponRow = CouponRow(homeTeam, awayTeam, len(self.couponrows))
                self.couponrows.append(newCouponRow)
        
        def sortListBasedOnMatchOrder(self):
                #Sorterar listan efter matchordning. Precis som den är på kupongen helt enkelt
                self.couponrows.sort(key = operator.attrgetter('matchnumber'))

        
        
        def sortBestHomeTeams(self):
                #Sorterar listann efter bästa sannlikhet att vinna på hemmaplan. 
                #Sorterar först listan och ger sedan varje rad sitt index i fältet homeProbOrder
                self.couponrows.sort(key = operator.attrgetter('homeProb'),reverse=True)
                i=1
                for row in self.couponrows:
                        row.homeProbOrder = i
                        i+=1
        
        def sortBestAwayTeams(self):
                #Sorterar listann efter bästa sannlikhet att vinna på bortaplan. 
                #Sorterar först listan och ger sedan varje rad sitt index i fältet awayProbOrder
                self.couponrows.sort(key = operator.attrgetter('awayProb'),reverse=True)
                i=1
                for row in self.couponrows:
                        row.awayProbOrder = i
                        i+=1


        def sortBestDrawTeams(self):
                #Sorterar listann efter bästa sannolikhet för att spela oavgjort. 
                #Sorterar först listan och ger sedan varje rad sitt index i fältet drawProbOrder
                self.couponrows.sort(key = operator.attrgetter('drawProb'),reverse=True)
                i=1
                for row in self.couponrows:
                        row.drawProbOrder = i
                        i+=1

        def addSigns(self, intOne, intDraw, intTwo):
                #Vilken prio skall tecknen ha?
                for row in self.couponrows:
                        if row.homeProbOrder <= intOne:
                                row.one = "1"
                        if row.awayProbOrder <= intTwo:
                                row.two = "2"
                        if row.drawProbOrder <= intDraw:
                                row.ex = "X"
                        row.combined = row.one + row.ex + row.two


        def printCoupon(self):
                for i in self.couponrows:
                        print(str(i.matchnumber) +":"+ i.homeTeam +"-"+i.awayTeam+","+i.combined)

        def createPayloadMessage(self):
                s = ""
                for i in self.couponrows:
                        s = s+"\n"+str(i.matchnumber) +":"+ i.homeTeam +"-"+i.awayTeam+","+i.combined
                return s
