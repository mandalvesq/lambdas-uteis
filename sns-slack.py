import json
import logging
import os
from urllib2 import Request, urlopen, URLError, HTTPError
# Read environment variables
logger = logging.getLogger()
logger.setLevel(logging.INFO)
def lambda_handler(event, context):
    logger.info("Event: " + str(event))
    # Read message posted on SNS Topic
    message = json.loads(event['Records'][0]['Sns']['Message'])
    logger.info("Message: " + str(message))
# Construct a slack message
    slack_message = {
        'channel': '#',
        'username': 'webhookbot',
        'text': "%s" % (message)
    }
# Post message on SLACK_WEBHOOK_URL
    req = Request('', json.dumps(slack_message))
    try:
        response = urlopen(req)
        response.read()
        logger.info("Message posted to %s", slack_message['channel'])
    except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)
    except URLError as e:
        logger.error("Server connection failed: %s", e.reason)
