numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

half_numbers = []

for number in numbers.values():
    half = number // 2
    half_numbers.append(half)

print(half_numbers)