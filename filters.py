def build_filter_expression(pk_value, pk_mode, sk_value, sk_mode, additional_filters):
    expr_vals = {}
    expressions = []

    if pk_value:
        expr_vals[':pk'] = pk_value
        expressions.append({
            'Exact': 'PK = :pk',
            'Begins with': 'begins_with(PK, :pk)',
            'Contains': 'contains(PK, :pk)'
        }[pk_mode])

    if sk_value:
        expr_vals[':sk'] = sk_value
        expressions.append({
            'Exact': 'SK = :sk',
            'Begins with': 'begins_with(SK, :sk)',
            'Contains': 'contains(SK, :sk)'
        }[sk_mode])

    for idx, f in enumerate(additional_filters, start=1):
        key = f":af{idx}"
        expr_vals[key] = f['Value']
        expressions.append({
            'Exact': f"{f['Field']} = {key}",
            'Begins with': f"begins_with({f['Field']}, {key})",
            'Contains': f"contains({f['Field']}, {key})"
        }[f['Mode']])

    return ' AND '.join(expressions), expr_vals
