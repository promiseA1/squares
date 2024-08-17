import time

def lower_case_letter():
    current_time = time.time()

    fractional_part = current_time - int(current_time)

    random_index = int(fractional_part * 26)

    random_letter = chr(97 + random_index)

    return random_letter



print(lower_case_letter())