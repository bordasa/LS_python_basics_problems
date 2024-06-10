def starts_with(word, prefix):
    if prefix in word:
        pre_len = len(prefix)
        return word[:pre_len] == prefix
    
    return False

    # suggested solution
    #return string.startswith(prefix)

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True