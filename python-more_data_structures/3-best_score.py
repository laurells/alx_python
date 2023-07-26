def best_score(a_dictionary):
    best_student = None
    best_score = None
    
    for student, score in a_dictionary.items():
        if best_score is None or score > best_score:
            best_score = score
            best_student = student
            
    return best_score