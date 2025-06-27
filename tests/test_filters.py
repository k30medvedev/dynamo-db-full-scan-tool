from filters import build_filter_expression

def test_build_filter_expression_exact():
    expr, vals = build_filter_expression('123', 'Exact', '456', 'Exact', [])
    assert 'PK = :pk' in expr
    assert 'SK = :sk' in expr
    assert vals[':pk'] == '123'
    assert vals[':sk'] == '456'

def test_build_filter_expression_with_additional():
    additional = [{'Field': 'status', 'Value': 'active', 'Mode': 'Exact'}]
    expr, vals = build_filter_expression(None, 'Exact', None, 'Exact', additional)
    assert 'status = :af1' in expr
    assert vals[':af1'] == 'active'
