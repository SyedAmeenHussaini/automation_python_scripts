import requests
import json
import os

def lambda_handler(event, context):
    endpoints = [
        "https://app.xyz.in/health-check",
        "https://staging-xyz.in/health-check",
        "https://api.xyz.in/health-check",
        "https://staging-api.xyz.in/health-check"
    ]

    slack_webhook_url = os.environ.get('SLACK_WEBHOOK_URL')

    # Check if webhook_url is None
    if not slack_webhook_url:
        print("SLACK_WEBHOOK_URL is not set.")
        return

    for endpoint in endpoints:
        try:
            # Check if endpoint is reachable with a timeout of 10 seconds
            response = requests.get(endpoint, timeout=10)
            response.raise_for_status()

        except requests.RequestException as e:
            # Endpoint is unreachable
            message = f"❌ Endpoint {endpoint} is unreachable. Error: {str(e)}"
            send_slack_notification(message, slack_webhook_url)

    # All endpoints are reachable
    print("✅ All endpoints are reachable.")

def send_slack_notification(message, webhook_url):
    payload = {"text": message}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()

    except requests.RequestException as e:
        print(f"Error sending Slack notification: {str(e)}")

    # Log the response if needed
    print("Slack API Response:", response.text)

