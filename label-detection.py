# coding: utf-8
import boto3
session = boto3.Session(profile_name='dynamodb')
s3 = session.resource('s3')
bucket = s3.create_bucket(Bucket='robinvideoly')
get_ipython().run_line_magic('ls', '/Users/nofam/Downloads/*.mp4')
pathname = '
pathname = '/Users/nofam/Downloads/Blurry Video Of People Working.mp4'
path = Path(pathname).expanduser().resolve()
for pathlib import Path
from pathlib import Path
path = Path(pathname).expanduser().resolve()
print(path)
bucket.upload_file(str(path), str(path.name))
rekognition_client = session.client('rekognition')
response = rekognition_client.start_label_detection(Video={'S3Object' : { 'Bucket' : bucket.name, 'Name': path.name}})
response
job_id = response['JobId']
result = rekognition_client.get_label_detection(JobId=job_id)
result.keys()
result.JobStatus
result.JobStatus()
result['JobStatus']
result['ResponseMetadata']
result['Labels']
len(result['Labels'])
