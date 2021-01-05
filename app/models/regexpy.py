import re

def checkRegex(form):
    name = postalCode = email = password = number = "Não preencheu!"
    if form["name"]: name = checkName(form["name"])
    if form["number"]: number = checkNumber(form["number"])
    if form["email"]: email = checkEmail(form["email"])
    if form["password"]: password = checkPassword(form["password"])
    if form["postalCode"]: postalCode = checkPostal(form["postalCode"])
    return {"name":name,"number":number,"email":email,"password":password,"postalCode":postalCode}

def checkEmail(string):
    regex = r'^([\w\.-]+[@]\w+[.]\w{2,})$'
    x = re.match(regex, string)
    if x:
        return 'E-mail válido'
    else:
        return 'E-mail não aceite'

def checkName(string):
    regex = r'^[a-zA-Z\s]*$'
    x = re.match(regex, string)
    if x:
        return 'Nome válido'
    else:
        return 'Nome não aceite'
def checkPassword(string):
    regex  = r'^(?=.*[A-Z])(?=(?:.*[a-z]){3})(?=.*\d)(?=\S{6,})(?=.*\W)(?!.*\s+)'

    x = re.match(regex, string)
    if x:
        return 'Password válida'
    else:
        return 'Password não aceite'
    
def checkNumber(string):
    regex = r'^[2789][\d]{8}$'

    if re.match(regex,string):
        return 'Número válido'
    else:
        return 'Número inválido'
        
def checkPostal(string):
    regex = r'^[0-9]{4}-[0-9]{3}$'

    if re.match(regex,string):
        return 'postal válido'
    else:
        return 'postal inválido'