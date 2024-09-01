# numeros romanos a valores decimales
roman_numeral_map = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9, 
    'V': 5, 
    'IV': 4, 
    'I': 1
}

def roman_to_int(roman):
    total = 0
    i = 0
    while i < len(roman):
        if (i + 1 < len(roman)) and (roman[i:i + 2] in roman_numeral_map):
            total += roman_numeral_map[roman[i:i + 2]]
            i += 2
        else:
            total += roman_numeral_map[roman[i]]
            i += 1
    return total

def extract_roman_numerals(word):
    roman_letters = ''
    
    # Iteracion de la palabra
    for char in word.upper():
        if char in roman_numeral_map:
            roman_letters += char

    # Convertir las letras extraidas a entero
    total = 0
    last_value = 0 

    # sumar los valores validos
    for char in roman_letters:
        current_value = roman_numeral_map[char]
        # Solo sumar si es menor o igual
        if current_value <= last_value or total == 0: 
            total += current_value
        last_value = current_value 

    # Ajuste para evitar combinaciones no válidas
    if 'IX' in roman_letters: 
        total = 9
    elif 'IV' in roman_letters and last_value == roman_numeral_map['C']: 
        total = 104

    return total

# Ejemplo de uso
words = ["pixel", "hijo", "toxico", "paco", "civil", "clave", "lili"]
for word in words:
    print(f'{word}: {extract_roman_numerals(word)}')
