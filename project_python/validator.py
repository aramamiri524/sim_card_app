import re
def sim_validator(sim):
    errors = []
    if not (type(sim[0]) == int and sim[0] > 0):
        errors.append("Sim ID must be an integer > 0")

    if not (type(sim[1]) == str and re.match(r"^09\d{9}$", sim[1])):
        errors.append("Number must be a valid Iranian mobile number (11 digits starting with 09)")

    if not (type(sim[2]) == str and re.match(r"^[a-zA-Z\s]{3,20}$", sim[2])):
        errors.append("Operator name is invalid")

    if not (type(sim[3]) == int and sim[3] >= 0):
        errors.append("Price must be a non-negative integer")

    if not (type(sim[4]) == int and sim[4] >= 0):
        errors.append("Charge must be a non-negative integer")

    if not (type(sim[5]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", sim[5])):
        errors.append("Owner name is invalid")

    return errors
