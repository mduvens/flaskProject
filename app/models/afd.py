def checkAutomato(sequencia):
    alfabeto = {"0","1"}
    estados = {"A","B","C","D"}
    estadoInicial = "A"
    estadosAceitacao = {"B"}
    tabelaTrans = { 
        ("A","0"):"B", # (atualEstado,simbolo): novoEstado
        ("A","1"):"D",
        ("B","0"):"B",
        ("B","1"):"C",
        ("C","0"):"B",
        ("C","1"):"C",
        ("D","0"):"D",
        ("D","1"):"D"
    }
    estado = estadoInicial
    for e in sequencia:
        if e in alfabeto:
            estado = tabelaTrans[estado,e]
        else:
            return "Nao corresponde ao alfabeto"
            break  
    else:    
        if estado in estadosAceitacao:
            return "Aceite"
        else:
            return "Não aceite"