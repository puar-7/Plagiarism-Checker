import re

def normalize_code(code):
    code = re.sub(r'//.*?(\n|\r\n)', '', code)  # remove single-line comments
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)  # remove block comments
    code = re.sub(r'\s+', ' ', code)  # remove excess whitespace
    return code

def rule_based_checker(code1, code2):
    code1 = normalize_code(code1)
    code2 = normalize_code(code2)
    
    return code1 == code2
