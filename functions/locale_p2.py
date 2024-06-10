def extract_region(language_code):
    #return language_code[3:5]

    # suggested solution:
    return language_code.split('.')[0].split('_')[1]

print(extract_region('en_US.UTF-8'))
print(extract_region('en_GB.UTF-8'))
print(extract_region('ko_KR.UTF-16'))
