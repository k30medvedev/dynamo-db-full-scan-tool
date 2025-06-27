from aws_client import create_session

def test_create_session():
    session = create_session('key', 'secret', 'token', 'eu-central-1')
    assert session.region_name == 'eu-central-1'
