# Lambda Health Check and Slack Notification

## Overview
This Python script performs health checks on multiple endpoints and sends notifications to a Slack channel if any endpoint is unreachable. It's designed to be used as an AWS Lambda function triggered by an event source (e.g., CloudWatch Events).

## Features
- Performs health checks on the specified endpoints.
- Sends notifications to a Slack channel using a webhook if any endpoint is unreachable.
- Supports customization through environment variables.

## Prerequisites
- Python 3.x installed on your local machine for testing.
- An AWS account with access to AWS Lambda and the ability to set up environment variables.
- A Slack workspace with a configured incoming webhook URL.

## Usage
1. Clone the repository:

2. Install the required Python packages:

    ```bash
    pip install requests
    ```

3. Configure the following environment variables:
   - `SLACK_WEBHOOK_URL`: The Slack webhook URL for sending notifications.

4. Test the script locally (optional):

    ```bash
    python lambda_health_check.py
    ```

5. Deploy the script as an AWS Lambda function and configure the trigger (e.g., CloudWatch Events).

6. Monitor the Slack channel for notifications about unreachable endpoints.

## Customization
- You can add or remove endpoints from the `endpoints` list in the script to match your environment.
- Adjust the timeout value for the HTTP requests as needed.
- Modify the message format sent to Slack in the `send_slack_notification` function.

## Additional Notes
- Ensure that the Lambda execution role has the necessary permissions to send HTTP requests and write logs.
- Monitor CloudWatch Logs for Lambda function execution logs.
- This script can be integrated into any AWS deployment pipeline or monitoring system for proactive alerting.


