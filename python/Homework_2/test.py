def topping1(dictionary):
    if "ice cream" in dictionary:
        dictionary["ice cream"] = "cherry"
    if "bread" in dictionary:
       dictionary["bread"] = "butter"
    else:
        dictionary["bread"] = "butter"
    return dictionary

print(topping1({"ice cream": "peanuts"}))