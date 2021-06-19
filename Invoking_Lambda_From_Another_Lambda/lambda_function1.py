import json, boto3

def lambda_handler(event, context):
    # TODO implement
    invokeLam = boto3.client("lambda")
    payload = {"message":"Hi, you have been invoked"}
    resp = invokeLam.invoke(FunctionName="lambda_function2", InvocationType="RequestResponse", Payload= json.dumps(payload))
    print(resp['Payload'].read())
    return 'Hello from lambda 1'
