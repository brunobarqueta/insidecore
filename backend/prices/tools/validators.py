def string_is_empty(string:str) -> bool:
    return string == ''

def string_isnull_or_whitespace(string:str) -> bool:
    return not string

def all_properies_nullables(*props) -> bool:
    for prop in props:
        if prop is not None:
            return False
    return True