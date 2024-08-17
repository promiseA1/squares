import time

def random_case_letter():
    current_time = time.time()
    fractional_part = current_time - int(current_time)

    #calculate the pseudo random index based on the fractional part
    random_index = int(fractional_part * 26)

    #generate the upper case letter using the ASCII values
    random_letter = chr(65 + random_index)

    return random_letter


print(random_case_letter())