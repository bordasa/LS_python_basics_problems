def is_empty_or_blank(string1):
    return not string1 or string1.isspace()

    # launch school solution
    #return string1.strip(' ') == ''

    # or more 'pythonic' solution
    #return not string1.strip(' ')

print(is_empty_or_blank('mars'))
print(is_empty_or_blank('    '))
print(is_empty_or_blank(''))