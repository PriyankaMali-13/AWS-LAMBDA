import json

def lambda_handler(event, context):
    # TODO implement
    a=10
    b=30
    result = a+b
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
