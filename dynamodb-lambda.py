#lambda function to read data from dynamodb table 
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('planet')

def lambda_handler(event, context):
    # TODO implement
    response = table.get_item(
        Key = {
            'id' : 'earth'
        }
    )
    return {
        'statusCode': 200,
        'body': response
    }
