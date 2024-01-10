from couponRow import *
import operator

class Coupon:
        def __init__(self):
                #Initierar en kupong som på det hela taget bara innehåller en array med rader.
                self.couponrows = []

        def addCouponRow(self, home_team, away_team, numberofRowsinArray):
        # Add a row to the coupon.
                coupon_row = CouponRow(home_team, away_team, numberofRowsinArray)
                self.couponrows.append(coupon_row)

        def getRows(self):
                # Return the coupon rows.
                return self.couponrows

        #min egna gamla CouponRow
        #def addCouponRow(self, homeTeam, awayTeam):
        #        newCouponRow = CouponRow(homeTeam, awayTeam, len(self.couponrows))
        #        self.couponrows.append(newCouponRow)
        
        def sortListBasedOnMatchOrder(self):
                #Sorterar listan efter matchordning. Precis som den är på kupongen helt enkelt
                self.couponrows.sort(key = operator.attrgetter('matchnumber'))

        
        
        def sortBestHomeTeams(self):
                #Sorterar listan efter bästa sannlikhet att vinna på hemmaplan. 
                #Sorterar först listan och ger sedan varje rad sitt index i fältet homeProbOrder
                self.couponrows.sort(key = operator.attrgetter('homeProb'),reverse=True)
                i=1
                for row in self.couponrows:
                        row.homeProbOrder = i
                        i+=1
        
        def sortBestAwayTeams(self):
                #Sorterar listan efter bästa sannlikhet att vinna på bortaplan. 
                #Sorterar först listan och ger sedan varje rad sitt index i fältet awayProbOrder
                self.couponrows.sort(key = operator.attrgetter('awayProb'),reverse=True)
                i=1
                for row in self.couponrows:
                        row.awayProbOrder = i
                        i+=1


        def sortBestDrawTeams(self):
                #Sorterar listan efter bästa sannolikhet för att spela oavgjort. 
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
                        print(str(i.matchnumber) +":"+ i.homeTeam +"-"+i.awayTeam+"["+i.homeProb+":"+i.drawProb+":"+i.awayProb+"]:"+i.combined)

        def createPayloadMessage(self):
                #För meddelande till Slack
                s = ""
                for i in self.couponrows:
                        s = s+"\n"+str(i.matchnumber) +":"+ i.homeTeam +"-"+i.awayTeam+","+i.combined
                return s
        
        def printDebugInfo(self):
                #Endast för debugsyfte
                print("Coupon Debug Info:")
                print("Number of Rows:", len(self.couponrows))
                for i, row in enumerate(self.couponrows):
                    print(f"Row {i + 1} - Match: {row.matchnumber}, Teams: {row.homeTeam}-{row.awayTeam}, Combined: {row.combined}")
                    print(f"   Home Prob Order: {row.homeProb}, Away Prob Order: {row.awayProb}, Draw Prob Order: {row.drawProb}")
                    print(f"   1: {row.one}, X: {row.ex}, 2: {row.two}")
                    print("")
