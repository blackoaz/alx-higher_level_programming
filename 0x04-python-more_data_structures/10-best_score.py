#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None 
    best_score = 0
    for k, v in a_dictionary.items():
        if v > best_score:
            best_score = v
    return best_score

