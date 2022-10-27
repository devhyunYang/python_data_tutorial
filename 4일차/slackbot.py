import requests
import json

def send_slack_message():
    slack_url = "https://hooks.slack.com/services/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"
    message = """메세지 전송""" 

    payloads = {
        "text": message,
        "username": "수업 신청",
        "icon_emoji": ":clap:"
    }

    response = requests.post(
        slack_url, data=json.dumps(payloads),
        headers={'Content-Type': 'application/json'}
    )

    if response.status_code != 200:
        print("error" + response.status_code)