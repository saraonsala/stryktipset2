from webscraping import getNext13Games
from competition import *
from coupon import *
from sendToSlack import *
from links import *

print("Startar Pelles fotbollsprogram 2.0 - Stryktipset...")

premierLeague = Competition(strPremierLeague)
championship = Competition(strChampionship)

thisCoupon = Coupon()
getNext13Games(thisCoupon, strPremierLeague, strChampionship)
#Hämtar sannolikhet för alla rader
for row in thisCoupon.couponrows:
    if premierLeague.isTeamInCompetition(row.awayTeam):
        premierLeague.getAllResults(row)
    elif championship.isTeamInCompetition(row.awayTeam):
        championship.getAllResults(row)
thisCoupon.sortBestHomeTeams()
thisCoupon.sortBestAwayTeams()
thisCoupon.sortBestDrawTeams()
thisCoupon.sortListBasedOnMatchOrder()
#Nästkommande funktion har möjligheten att ange hur många 1 X 2 man vil ha)?
thisCoupon.addSigns(6,4,4)
#thisCoupon.printCoupon()

webhook = strSlackWebhook
payload = {"text": thisCoupon.createPayloadMessage()}
send_slack_message(payload, webhook)