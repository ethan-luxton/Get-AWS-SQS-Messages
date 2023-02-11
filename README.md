# Get-AWS-SQS-Messages

## Retreives SQS Message Data through Python Boto3 AWS-SDK

## Requirements

* dotenv
    * pip install python-dotenv
* boto3
    * pip install boto3
* os
* json

## ENV Requirements

* AWS_DEFAULT_REGION=your-default-region
* AWS_ACCESS_KEY_ID=your-access-key
* AWS_SECRET_ACCESS_KEY=your-secret-access-key
* QUEUE_URL=https://sqs.{region}.amazonaws.com/{user_id}/{queue_name}
    * Replace the Queue URL with your own AWS SQS Queue URL.

### How it works

* Attribute names is by default set to 'All', this can be set according to what data you want to pull. 

* MaxNumberOfMessages is set to 10 by default, this can be changed depending on needs.

* To run: In your terminal, type:
    * ```python getAWSmessages.py```

* In your terminal it will return prettified JSON data of your first [X amount] of messages.