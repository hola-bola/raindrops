def convert(number):
    string = ""
    if number % 3 == 0:
        string += 'Pling'
    if number % 5 == 0:
        string += 'Plang'
    if number % 7 == 0:
        string += 'Plong'
    if number % 7 and number % 5 and number % 3:
        return str(number)

    return string


print(convert(30))
