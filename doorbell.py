def ring(number_of_knocks):
    doorbell_response = ""

    if number_of_knocks % 3 == 0:
        doorbell_response = doorbell_response + "Ding"
    if number_of_knocks % 5 == 0:
        doorbell_response = doorbell_response + "Dang"
    if number_of_knocks % 7 == 0:
        doorbell_response = doorbell_response + "Dong"
    if doorbell_response == "":
        return number_of_knocks
    return doorbell_response

