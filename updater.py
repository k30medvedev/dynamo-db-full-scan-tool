from decimal import Decimal

def build_update_expression(update_fields):
    update_parts, update_vals = [], {}
    for idx, f in enumerate(update_fields, start=1):
        fld, val, typ = f['Field'], f['Value'], f['Type']
        if not fld or not val or fld in ['PK', 'SK']:
            continue
        placeholder = f":u{idx}"
        if typ == 'Number':
            update_vals[placeholder] = Decimal(val)
        elif typ == 'Boolean':
            update_vals[placeholder] = val.lower() in ['true', '1', 'yes']
        else:
            update_vals[placeholder] = val
        update_parts.append(f"{fld} = {placeholder}")
    return "SET " + ", ".join(update_parts), update_vals
