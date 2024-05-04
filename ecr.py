#code that create ecr repository that hold our docker image 

import boto3  #sdk in python to create , configure and manage aws services 

ecr_client = boto3.client('ecr')

repository_name = "my_monitoring_app_image"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response ['repository']['repositoryUri']
print(repository_uri)