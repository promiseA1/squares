def character_of_an_ascii_code(code):
    character_of_an_ascii_code = chr(code)
    return character_of_an_ascii_code

code = eval(input("Enter an ascii code between 0 and 127: "))
print(character_of_an_ascii_code(code))