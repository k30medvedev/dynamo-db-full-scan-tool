import pandas as pd

def scan_table(table):
    items, sk = [], None
    while True:
        resp = table.scan(ExclusiveStartKey=sk) if sk else table.scan()
        items.extend(resp.get('Items', []))
        sk = resp.get('LastEvaluatedKey')
        if not sk:
            break
    return pd.DataFrame(items)

def count_records(table):
    total, sk = 0, None
    while True:
        resp = table.scan(Select='COUNT', ExclusiveStartKey=sk) if sk else table.scan(Select='COUNT')
        total += resp.get('Count', 0)
        sk = resp.get('LastEvaluatedKey')
        if not sk:
            break
    return total
