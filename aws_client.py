import boto3
from botocore.config import Config

def create_session(aws_access_key_id, aws_secret_access_key, aws_session_token, region_name):
    return boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token,
        region_name=region_name
    )

def get_dynamodb_table(session, table_name):
    return session.resource(
        service_name='dynamodb',
        config=Config(signature_version='v4')  # Safe default
    ).Table(table_name)