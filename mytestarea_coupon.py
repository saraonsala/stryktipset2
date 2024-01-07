from coupon import * 
from links import * 
from webscraping import *


# Print debug information
premierLeague = Competition(strPremierLeague)
championship = Competition(strChampionship)

myCoupon = Coupon()
getNext13Games(myCoupon, premierLeague, championship)
myCoupon.printDebugInfo()