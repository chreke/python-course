NUMERALS = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]

def roman_numeral(integer):
    numeral = ""
    for (value, letter) in NUMERALS:
        qty = integer // value
        numeral += letter * qty
        integer -= qty * value
    return numeral

def numeral_to_int(numeral):
    integer = 0
    for (value, letter) in NUMERALS:
        while numeral.startswith(letter):
            integer += value
            numeral = numeral[len(letter):]
    return integer
