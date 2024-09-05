import ast

def get_code_structure(code):
    """
    Parse the code and return its structure as a string.
    """
    try:
        tree = ast.parse(code)
        return ast.dump(tree)
    except SyntaxError:
        # Handle cases where the input code isn't valid Python code
        return None

def structural_similarity_checker(code1, code2):
    """
    Compare the structural similarity of two code snippets using AST.
    """
    structure1 = get_code_structure(code1)
    structure2 = get_code_structure(code2)
    
    # If either code cannot be parsed, return False
    if structure1 is None or structure2 is None:
        return False
    
    return structure1 == structure2
