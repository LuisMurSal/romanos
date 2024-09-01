import re

# numeros romanos a valor decimal
roman_numeral_map = {
    'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
    'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 
    'V': 5, 'IV': 4, 'I': 1
}

def roman_to_int(roman):
    i = 0
    num = 0
    while i < len(roman):
        if i + 1 < len(roman) and roman[i:i + 2] in roman_numeral_map:
            num += roman_numeral_map[roman[i:i + 2]]
            i += 2
        else:
            num += roman_numeral_map[roman[i]]
            i += 1
    return num

def extract_roman_numerals(word):
    roman_letters = ''
    i = 0
    while i < len(word):
        # extraer pares de letras o letras individuales que sean validas
        if i + 1 < len(word) and word[i:i + 2].upper() in roman_numeral_map:
            roman_letters += word[i:i + 2].upper()
            i += 2
        elif word[i].upper() in roman_numeral_map:
            roman_letters += word[i].upper()
            i += 1
        else:
            i += 1
    
    # convertir las letras o letra extraida a numero entero
    return roman_to_int(roman_letters)

def sort_by_roman_numerals(words):
    return sorted(words, key=lambda word: extract_roman_numerals(word))

# uso con algunos ejemplos
words = ["Lili", "toxico", "paco", "clave"]
sorted_words = sort_by_roman_numerals(words)

for word in sorted_words:
    print(f'{word}: {extract_roman_numerals(word)}')
