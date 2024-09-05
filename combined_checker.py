from rule_based_checker import rule_based_checker
from bert_similarity_checker import bert_similarity_checker
from structural_checker import structural_similarity_checker

def combined_plagiarism_checker(code1, code2):
    # First, try rule-based plagiarism detection
    if rule_based_checker(code1, code2):
        return True
    
    # Use structural similarity as an additional filter
    if structural_similarity_checker(code1, code2):
        return True
    
    # Use AI-enhanced detection (BERT embeddings)
    similarity = bert_similarity_checker(code1, code2)
    return similarity > 0.95
