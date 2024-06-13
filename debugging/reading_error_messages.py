def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0) #this needs to be a single list, can add brackets around the given list or make a new variable
find_first_nonzero_among(1) #a single integer is not iterable, so thiw will raise a type error unless it is in [] as well