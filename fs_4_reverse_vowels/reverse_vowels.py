def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?'' 
    """
    revstring = ""
    newstring =""
    for x in s:
        if x.lower() in "aeiou":
            revstring = revstring+x
    revstring= revstring[len(revstring)-1::-1]
    for x in s:
        if x.lower() in "aeiou":
            newstring = newstring+revstring[0]
            revstring = revstring[1:]
        else:
            newstring = newstring+x
    return newstring

  