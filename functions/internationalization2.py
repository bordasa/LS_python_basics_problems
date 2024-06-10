def extract_language(language_code):
    #return language_code[:2]
    
    # suggested solution
    return language_code.split('_')[0]

def extract_region(language_code):
    #return language_code[3:5]

    # suggested solution:
    return language_code.split('.')[0].split('_')[1]

def local_greet(lang_code):
    
    language = extract_language(lang_code)
    region = extract_region(lang_code)
    
    match language:
        case 'en':
            match region:
                case 'US':
                    return 'Hey!'
                case 'GB':
                    return 'Hello!'
                case 'AU':
                    return 'Howdy!'
                case _:
                    return 'Hi!'
        case 'fr':
            match region:
                case _:
                    return 'Salut!'
        case 'pt':
            match region:
                case _:
                    return 'Olá!'
        case 'de':
            match region:
                case _:
                    return 'Hallo!'
        case 'sv':
            match region:
                case _:
                    return 'Hej!'
        case 'af':
            match region:
                case _:
                    return 'Haai!'
        case _:
            return 'Hello, this language code is not recognized.'