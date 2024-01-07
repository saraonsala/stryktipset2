from webscraping import getNext13Games
from competition import *
from coupon import *
from sendToSlack import *

print("Startar Pelles fotbollsprogram 2.0 - Stryktipset...")
#testar
#URL:er till csv-filer online
urlPremierLeague = "https://www.football-data.co.uk/mmz4281/2223/E0.csv"
urlChampionship = "https://www.football-data.co.uk/mmz4281/2223/E1.csv"

premierLeague = Competition(urlPremierLeague)
championship = Competition(urlChampionship)

thisCoupon = Coupon()
getNext13Games(thisCoupon, premierLeague, championship)
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

webhook = "https://hooks.slack.com/services/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"
payload = {"text": thisCoupon.createPayloadMessage()}
send_slack_message(payload, webhook)