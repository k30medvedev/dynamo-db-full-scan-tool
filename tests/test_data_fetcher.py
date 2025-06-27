from data_fetcher import scan_table, count_records

def test_scan_table(dynamo_table):
    df = scan_table(dynamo_table)
    assert len(df) == 2

def test_count_records(dynamo_table):
    count = count_records(dynamo_table)
    assert count == 2
