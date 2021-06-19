import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('planet')

def lambda_handler(event, context):
    # TODO implement
    table.put_item(
        Item = {
            'id' : 'neptune',
            'temp' : 'super cold'
        }
        
        )
    return {
        'statusCode': 200,
        'body': 'Item Created'
    }
