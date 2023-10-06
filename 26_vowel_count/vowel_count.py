def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowct = {}
    vow ='aeiou'
    for ch in phrase:
        if ch.lower() in vow:
            if ch.lower() in vowct.keys():
                vowct[ch.lower()] += 1
            else: 
                vowct[ch.lower()] = 1    
    return vowct
        

