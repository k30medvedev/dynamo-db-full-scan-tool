from updater import build_update_expression

def test_build_update_expression():
    fields = [
        {'Field': 'name', 'Value': 'test', 'Type': 'String'},
        {'Field': 'count', 'Value': '5', 'Type': 'Number'},
        {'Field': 'active', 'Value': 'true', 'Type': 'Boolean'}
    ]
    expr, vals = build_update_expression(fields)
    assert 'name = :u1' in expr
    assert 'count = :u2' in expr
    assert 'active = :u3' in expr
    assert vals[':u1'] == 'test'
    assert str(vals[':u2']) == '5'
    assert vals[':u3'] is True
