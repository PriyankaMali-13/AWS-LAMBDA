#Creating lambda function that gets triggers when a file is 
# deleted or created in s3 bucket and sends an email notification to user
import json
import boto3


def lambda_handler(event, context):
    for i in event['Records']:
        action = i["eventName"]
        ip = i["requestParameters"]["sourceIPAddress"]
        bucket_name = i["s3"]["bucket"]["name"]
        object = i["s3"]["object"]["key"]

    client = boto3.client("ses")

    subject = str(action) + 'Event from ' + bucket_name
    body = """
        <br>
        This email is to notify you regarding {} event.
        The object {} is {}.
        Source IP: {}
    """.format(action, object, action, ip)

    message = {"Subject": {"Data": subject}, "Body": {"Html": {"Data": body}}}

    response =  client.send_email(Source = "priyankamali0000@gmail.com", Destination = {"ToAddresses": ["priyankamali0000@gmail.com"]}, Message = message)

    return "Thanks"