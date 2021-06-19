#Perform sentimental analysis using amazon comprehend with lambda
#Perform name entity recognition using amazon comprehend with lambda
#Perform key phrases extraction using amazon comprehend with lambda
import json, boto3
import pprint; 

def lambda_handler(event, context):
    s3 = boto3.client("s3")
    bucket_name = "comprehend-s3-send"
    file_name = "speech.txt"
    file = s3.get_object(Bucket = bucket_name, Key = file_name)
    paragraph = str(file['Body'].read())
    
    comprehend = boto3.client("comprehend")
    response = comprehend.detect_sentiment(Text = paragraph, LanguageCode = 'en')
    print("Sentiment", response)
    
    entities = comprehend.detect_entities(Text = paragraph, LanguageCode = 'en')
    pprint.pprint(entities)
    
    keyphrase = comprehend.detect_key_phrases(Text = paragraph, LanguageCode = 'en')
    pprint.pprint(keyphrase)
    
    return "Hello from lambda"