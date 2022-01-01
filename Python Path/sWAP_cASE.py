def swap_case(s):
    outStr = ""
    for letter in s:
        if letter.islower():
            outStr += letter.upper()
        elif letter.isupper():
            outStr += letter.lower()
        else:
            outStr += letter

    return outStr
