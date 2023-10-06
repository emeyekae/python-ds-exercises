def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_string = ""
    if to_swap.upper() in phrase.upper():
        for char in phrase:
            if char.upper() == to_swap.upper():
                new_string += char.swapcase()
            else: 
                new_string += char 
        return new_string
    


        
