

import json
import requests
from links import * 

def sendToSlack (thisCoupon):
   webhook = strSlackWebhook
   payload = {"text": thisCoupon.createPayloadMessage()}
   #"""Send a Slack message to a channel via a webhook. 
   return requests.post(webhook, json.dumps(payload))