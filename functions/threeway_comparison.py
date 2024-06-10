def compare_by_length(string1, string2):
    if len(string1) < len(string2):
        return -1
    elif len(string1) > len(string2):
        return 1
    else:
        return 0