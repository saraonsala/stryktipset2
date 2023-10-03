

import json
import requests


def send_slack_message(payload, webhook):
   #"""Send a Slack message to a channel via a webhook. 
    return requests.post(webhook, json.dumps(payload))