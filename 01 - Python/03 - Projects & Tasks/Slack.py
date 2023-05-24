import requests
import json

def send_slack_message(payload, webhook):

    return requests.post(webhook, json.dumps(payload))

webhook = "https://hooks.slack.com/services/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"
message = input("Enter the message: ")
payload = {"text": message}
send_slack_message(payload, webhook)