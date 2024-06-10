weather = 'sunny'

match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print('Grab your umbrella!')
    case 'snowy':
        print('Grab a coat!')
    case _:
        print("Let's stay inside.")