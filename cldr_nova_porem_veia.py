def calcular():
  
  def calculator_explain_expr():
    #definir a expressão que ira ser feita
    texto=input("digite um calculo, ex: (1 + 1 + 1): ")
    text=texto
    texto=texto.replace(",", ".")
    # substitue as operações em codigo para como comummente vemos
    if "**" in texto:
      texto=texto.replace("**", "^")
    elif "*" in texto:
      texto=texto.replace("*", "x")
    
    #setar a variavel etapa para usar na contagem de explicações
    etapa=0
    # colocar um espaço entre os numeros  e o operador para poder bota-los separados em uma lista
    if not " " in texto:
      if "+" in texto:
        texto=texto.replace("+", " + ")
      if "-" in texto:
          texto=texto.replace("-", " - ")
      if "||" in texto:
        texto=texto.replace("||", " || ")
      if "/" in texto:
        texto=texto.replace("/", " / ")
      if "x" in texto:
        texto=texto.replace("x", " x ")
      if "^" in texto:
        texto=texto.replace("^", " ^ ")

    # split para transformar a expressão em uma lista dividindo os valores, facilitando o calculo 
    texto=texto.split()
    print( )
    print("Expressão que você escolheu em formato de lista")
    print(texto)
    print( )
    while "||" in texto:
      first=int(texto.index("||"))
      index1=first+1
      x=float(texto[index1])
      result=x**(1/2)
      del texto[index1]
      del texto[first]
      texto.insert(first, str(result))
      etapa+=1
      print( )
      print(f"etapa {etapa}")
      print(texto)

    while "^" in texto:
      first=int(texto.index("^"))
      index1, index2= first-1, first+1
      x, y=float(texto[index1]), float(texto[index2])
      result=x**y
      del texto[index2]
      del texto[first]
      del texto[index1]
      texto.insert(first - 1, str(result))
      etapa+=1
      print( )
      print(f"etapa {etapa}")
      print(texto)

    while "x" in texto:
      first=int(texto.index("x"))
      index1, index2= first-1, first+1
      x, y=float(texto[index1]), float(texto[index2])
      result=x*y
      del texto[index2]
      del texto[first]
      del texto[index1]
      texto.insert(first - 1, str(result))
      etapa+=1
      print( )
      print(f"etapa {etapa}")
      print(texto)

    while "/" in texto:
      first=int(texto.index("/"))
      index1, index2= first-1, first+1
      x, y=float(texto[index1]), float(texto[index2])
      result=x/y
      del texto[index2]
      del texto[first]
      del texto[index1]
      texto.insert(first - 1, str(result))
      etapa+=1
      print( )
      print(f"etapa {etapa}")
      print(texto)

    while "+" in texto:
      first=int(texto.index("+"))
      index1, index2= first-1, first+1
      x, y=float(texto[index1]), float(texto[index2])
      result=x+y
      del texto[index2]
      del texto[first]
      del texto[index1]
      texto.insert(first - 1, str(result))
      etapa+=1
      print( )
      print(f"etapa {etapa}")
      print(texto)

    while "-" in texto:
      first=int(texto.index("-"))
      index1, index2= first-1, first+1
      x, y=float(texto[index1]), float(texto[index2])
      result=x-y
      del texto[index2]
      del texto[first]
      del texto[index1]
      texto.insert(first - 1, str(result))
      etapa+=1
      print( )
      print(f"etapa {etapa}")
      print(texto)

    result=f"{result:_.2f}"
    result=result.replace(".", ",").replace("_", ".")
    result_str=result[-3:]
    if result_str==",00":
        result_str_cplt=str(result)
        result=result_str_cplt.replace(result_str, " ")

    print( )
    print(f"Calculando por expressão numérica, oresultado de {text} é {result}")

  def calculator_expr():
      #definir a expressão que ira ser feita
    texto=input("digite um calculo, ex: (1 + 1 + 1): ")
    text=texto
    texto=texto.replace(",", ".")
    # substitue as operações em codigo para como comummente vemos
    if "**" in texto:
      texto=texto.replace("**", "^")
    elif "*" in texto:
      texto=texto.replace("*", "x")

    # colocar um espaço entre os numeros  e o operador para poder bota-los separados em uma lista
    if not " " in texto:
      if "+" in texto:
        texto=texto.replace("+", " + ")
      if "-" in texto:
          texto=texto.replace("-", " - ")
      if "||" in texto:
        texto=texto.replace("||", " || ")
      if "/" in texto:
        texto=texto.replace("/", " / ")
      if "x" in texto:
        texto=texto.replace("x", " x ")
      if "^" in texto:
        texto=texto.replace("^", " ^ ")

    # split para transformar a expressão em uma lista dividindo os valores, facilitando o calculo 
    texto=texto.split()

    while "||" in texto:
      first=int(texto.index("||"))
      index1=first+1
      x=float(texto[index1])
      result=x**(1/2)
      del texto[index1]
      del texto[first]
      texto.insert(first, str(result))

    while "^" in texto:
      first=int(texto.index("^"))
      index1, index2= first-1, first+1
      x, y=float(texto[index1]), float(texto[index2])
      result=x**y
      del texto[index2]
      del texto[first]
      del texto[index1]
      texto.insert(first - 1, str(result))

    while "x" in texto:
      first=int(texto.index("x"))
      index1, index2= first-1, first+1
      x, y=float(texto[index1]), float(texto[index2])
      result=x*y
      del texto[index2]
      del texto[first]
      del texto[index1]
      texto.insert(first - 1, str(result))

    while "/" in texto:
      first=int(texto.index("/"))
      index1, index2= first-1, first+1
      x, y=float(texto[index1]), float(texto[index2])
      result=x/y
      del texto[index2]
      del texto[first]
      del texto[index1]
      texto.insert(first - 1, str(result))

    while "+" in texto:
      first=int(texto.index("+"))
      index1, index2= first-1, first+1
      x, y=float(texto[index1]), float(texto[index2])
      result=x+y
      del texto[index2]
      del texto[first]
      del texto[index1]
      texto.insert(first - 1, str(result))

    while "-" in texto:
      first=int(texto.index("-"))
      index1, index2= first-1, first+1
      x, y=float(texto[index1]), float(texto[index2])
      result=x-y
      del texto[index2]
      del texto[first]
      del texto[index1]
      texto.insert(first - 1, str(result))

    result=f"{result:_.2f}"
    result=result.replace(".", ",").replace("_", ".")
    result_str=result[-3:]
    if result_str==",00":
        result_str_cplt=str(result)
        result=result_str_cplt.replace(result_str, " ")

    print(f"Calculando por expressão numérica, o resultado de {text} é {result}")

  def calcu_explain_ord():
    texto=input("digite um calculo, ex: (1 + 1 + 1): ")
    text=texto
    texto=texto.replace(",", ".")

    # substitue as operações em codigo para como comummente vemos
    if "**" in texto:
      texto=texto.replace("**", "^")
    elif "*" in texto:
      texto=texto.replace("*", "x")

    #setar a variavel etapa para usar na contagem de explicações
    etapa=0
    # colocar um espaço entre os numeros  e o operador para poder bota-los separados em uma lista
    if not " " in texto:
      if "+" in texto:
        texto=texto.replace("+", " + ")
      if "-" in texto:
          texto=texto.replace("-", " - ")
      if "||" in texto:
        texto=texto.replace("||", " || ")
      if "/" in texto:
        texto=texto.replace("/", " / ")
      if "x" in texto:
        texto=texto.replace("x", " x ")
      if "^" in texto:
        texto=texto.replace("^", " ^ ")

    texto=texto.split()
    print( )
    print("Operação separada em lista")
    print(texto)
    print( )

    while len(texto)>1:
      x, y=float(texto[0]), float(texto[2])
      escolha=texto[1]
      if escolha=="+":
        result=x+y
      elif escolha=="-":
        result=x-y
      elif escolha=="/":
        result=x/y
      elif escolha=="x":
        result=x*y
      elif escolha=="^":
        result=x**y
      del texto[2]
      del texto[1]
      del texto[0]
      texto.insert(0, result)
      etapa+=1
      print( )
      print(f"etapa {etapa}")
      print(texto)

    result=f"{result:_.2f}"
    result=result.replace(".", ",").replace("_", ".")
    result_str=result[-3:]
    if result_str==",00":
        result_str_cplt=str(result)
        result=result_str_cplt.replace(result_str, " ")
    print( )
    print(f"Calculando na ordem que aparece, o resultado de {text} é {result}")

  def calcu_ord():
    texto=input("digite um calculo, ex: (1 + 1 + 1): ")
    text=texto
    texto=texto.replace(",", ".")

    # substitue as operações em codigo para como comummente vemos
    if "**" in texto:
      texto=texto.replace("**", "^")
    elif "*" in texto:
      texto=texto.replace("*", "x")

    # colocar um espaço entre os numeros  e o operador para poder bota-los separados em uma lista
    if not " " in texto:
      if "+" in texto:
        texto=texto.replace("+", " + ")
      if "-" in texto:
          texto=texto.replace("-", " - ")
      if "||" in texto:
        texto=texto.replace("||", " || ")
      if "/" in texto:
        texto=texto.replace("/", " / ")
      if "x" in texto:
        texto=texto.replace("x", " x ")
      if "^" in texto:
        texto=texto.replace("^", " ^ ")

    texto=texto.split()
    print(texto)

    while len(texto)>1:
      x, y=float(texto[0]), float(texto[2])
      escolha=texto[1]
      if escolha=="+":
        result=x+y
      elif escolha=="-":
        result=x-y
      elif escolha=="/":
        result=x/y
      elif escolha=="x":
        result=x*y
      elif escolha=="^":
        result=x**y
      del texto[2]
      del texto[1]
      del texto[0]
      texto.insert(0, result)

    result=f"{result:_.2f}"
    result=result.replace(".", ",").replace("_", ".")
    result_str=result[-3:]
    if result_str==",00":
        result_str_cplt=str(result)
        result=result_str_cplt.replace(result_str, " ")

    print(f"Calculando na ordem que aparece, o resultado de {text} é {result}")

  #escolha do tipo de  calculadora
  s_n=input("Você quer calculadora por expressão numérica(1) ou na ordem que aparece(2)? ")
  s_n1=input("Você quer que a calculadora explique o calculo? (s/n)? ")

  if s_n=="1":
    if s_n1=="s":
      calculator_explain_expr()
    else:
      calculator_expr()
  elif s_n=="2":
      if s_n1=="s":
        calcu_explain_ord()
      else:
        calcu_ord()
calcular()