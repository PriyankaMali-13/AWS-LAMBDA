#Performing label detection on image
#Image Analysis 
#Creating lambda function go get trigger when an image is added to s3 bucket to do image anaylsis
#Basically it will give objects, name, people, text, scenes by looking at image
import boto3


def lambda_handler(event, context):

    client = boto3.client("rekognition")
    s3 = boto3.client("s3")

    # reading file from s3 bucket and passing it as bytes
    fileObj = s3.get_object(Bucket = "comprehend-s3-send", Key="image.jpg")
    file_content = fileObj["Body"].read()

    # passing bytes data
    response = client.detect_labels(Image = {"Bytes": file_content}, MaxLabels=3, MinConfidence=70)

    # passing s3 bucket object file reference
    response = client.detect_labels(Image = {"S3Object": {"Bucket": "comprehend-s3-send", "Name": "image.jpg"}}, MaxLabels=3, MinConfidence=70)    

    print(response)

    return "Thanks"