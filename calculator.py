def calculator():
#fazer uma calculadora que aceite expressãoo numerica e faça as 6 operações

    import math
    #definir a expressão que ira ser feita
    texto=input("digite um calculo, ex: (1 + 1) ou (1+1+1) obs: para raiz utilize '//(9)' : ")
    texto=texto.replace(",", ".")
    texto=texto.replace("//", "sqrt")

    
    try:
        #tenta fazer o que esta dentro dele, se der errado pula para o except
        resultado = (eval(texto, {"__builtins__": None}, {"sqrt": math.sqrt}))
    
        #os codigos desta linha até a 18 servem para retirar o ",00" do final se o numero for inteiro
        resultado=f"{resultado:_.2f}"
        resultado=resultado.replace(".", ",").replace("_", ".")
        resultado_str=resultado[-3:]
        if resultado_str==",00":
          resultado_str_cplt=str(resultado)
          resultado=resultado_str_cplt.replace(resultado_str, " ")

        # substitue as operações em codigo para como comumente vemos
        if "**" in texto:
          texto=texto.replace("**", "^")
        elif "*" in texto:
          texto=texto.replace("*", "x")
                                            
        #so para dar um espaçameento e deixar o codigo um pouco mais bonito
        if not " " in texto:
          if "+" in texto:
            texto=texto.replace("+", " + ")
          if "-" in texto:
              texto=texto.replace("-", " - ")
          if "/" in texto:
            texto=texto.replace("/", " / ")
          if "x" in texto:
            texto=texto.replace("x", " x ")
          if "^" in texto:
            texto=texto.replace("^", " ^ ")
       
        texto=texto.replace("sqrt", "//")

        #exibir a resposta
        print(f"O resultado de {texto} é: {resultado}")

    #se nao conseguir fazer as funções acima ele mostra erro de forma mais sultil ao acontecer algum bug
    except:
        print("Erro: Tente novamente.")
calculator()
