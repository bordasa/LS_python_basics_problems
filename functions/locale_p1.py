def extract_language(language_code):
    #return language_code[:2]
    
    # suggested solution
    return language_code.split('_')[0]


print(extract_language('en_US.UTF-8'))
print(extract_language('en_GB.UTF-8'))
print(extract_language('ko_KR.UTF-16'))
