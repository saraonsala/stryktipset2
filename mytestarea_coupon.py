from coupon import * 
from links import * 
from webscraping import *


# Printar debug information
myCoupon = Coupon()
premierLeague = Competition(strPremierLeague)
championship = Competition(strChampionship)
for row in myCoupon.couponrows:
    if premierLeague.isTeamInCompetition(row.awayTeam):
        premierLeague.getAllResults(row)
    elif championship.isTeamInCompetition(row.awayTeam):
        championship.getAllResults(row)
myCoupon.sortBestHomeTeams()
myCoupon.sortBestAwayTeams()
myCoupon.sortBestDrawTeams()
myCoupon.sortListBasedOnMatchOrder()
getNext13Games(myCoupon, premierLeague, championship)
myCoupon.printDebugInfo()