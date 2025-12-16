import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-0743b5f6166e8f22b').terminate() # put your instance id