"""This is the entry point of the program."""




def highest_number_cubed(limit):
    
    constant = 1 
    result = 0
    
    while result < limit:
        result = constant ** 3
        
        if result < limit:
            constant += 1
        if result > limit:
            constant = constant -1
            return constant

