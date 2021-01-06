import regex

def checkRegex(form):
    name = postalCode = email = password = number = "⚠️Não preencheu! "
    if form["name"]: name = checkName(form["name"])
    if form["number"]: number = checkNumber(form["number"])
    if form["email"]: email = checkEmail(form["email"])
    if form["password"]: password = checkPassword(form["password"])
    if form["postalCode"]: postalCode = checkPostal(form["postalCode"])
    return {"name":name,"number":number,"email":email,"password":password,"postalCode":postalCode}

def checkEmail(string):
    check = r'^([\w\.-]+[@]\w+[-]*\w+[.]\w{2,})$'
    x = regex.match(check, string)
    if x:
        return '✅E-mail válido'
    else:
        return '❌E-mail não aceite'

def checkName(string):
    check = r'^[a-zA-Z\s]*$'
    x = regex.match(check, string)
    if x:
        return '✅Nome válido'
    else:
        return '❌Nome não aceite'
def checkPassword(string):
    check  = r'^(?=.*[A-Z])(?=(?:.*[a-z]){3})(?=.*\d)(?=\S{6,})(?=.*\W)(?!.*\s+)'

    x = regex.match(check, string)
    if x:
        return '✅Password válida'
    else:
        return '❌Password não aceite'
    
def checkNumber(string):
    check = r'^[2789][\d]{8}$'

    if regex.match(check,string):
        return '✅Número válido'
    else:
        return '❌Número inválido'
        
def checkPostal(string):
    check = r'^[0-9]{4}[-\s][0-9]{3}$'

    if regex.match(check,string):
        return '✅Postal válido'
    else:
        return '❌Postal inválido'