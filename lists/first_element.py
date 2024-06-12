def first(my_list):
    if my_list:
        return my_list[0]
    else:
        return "List is empty."
    
print(first(['Earth', 'Moon', 'Mars']))  # Earth
print(first([]))