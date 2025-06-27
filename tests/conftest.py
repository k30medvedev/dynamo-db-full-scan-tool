import pytest
import boto3
from moto import mock_dynamodb

@pytest.fixture
def dynamo_table():
    with mock_dynamodb():
        client = boto3.resource('dynamodb', region_name='eu-central-1')
        table = client.create_table(
            TableName='TestTable',
            KeySchema=[
                {'AttributeName': 'PK', 'KeyType': 'HASH'},
                {'AttributeName': 'SK', 'KeyType': 'RANGE'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'PK', 'AttributeType': 'S'},
                {'AttributeName': 'SK', 'AttributeType': 'S'}
            ],
            BillingMode='PAY_PER_REQUEST'
        )
        table.put_item(Item={'PK': '1', 'SK': 'A'})
        table.put_item(Item={'PK': '2', 'SK': 'B'})
        yield table
