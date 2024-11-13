#definir a expressão que ira ser feita
texto=input("digite um calculo, ex: (1 + 1): ")

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
  if "/" in texto:
     texto=texto.replace("/", " / ")
  if "x" in texto:
    texto=texto.replace("x", " x ")
  if "^" in texto:
    texto=texto.replace("^", " ^ ")

# split para transformar a expressão em uma lista dividindo os valores, facilitando o calculo 
texto=texto.split()

x=float(str(texto[0]).replace(",", "."))

y=float(str(texto[2]).replace(",", "."))

escolha1=texto[1]

#execulta a operação de acordo com a escolha
if len(texto)>=3:
  x=float(str(texto[0]).replace(",", "."))
  y=float(str(texto[2]).replace(",", "."))
  escolha1=texto[1]
  if escolha1=="+":
    resultado=x+y
  elif escolha1=="-":
    resultado=x-y
  elif escolha1=="/":
    resultado=x/y
  elif escolha1=="x":
    resultado=x*y
  elif escolha1=="^":
    resultado=x**y
if len(texto)>=5:
  z=float(str(texto[4]).replace(",", "."))
  escolha2=texto[3]
  if escolha2=="+":
    resultado=resultado+z
  elif escolha2=="-":
    resultado=resultado-z
  elif escolha2=="/":
    resultado=resultado/z
  elif escolha2=="x":
    resultado=resultado*z
  elif escolha2=="^":
    resultado=resultado**z
if len(texto)>=7:
  a=float(str(texto[6]).replace(",", "."))
  escolha3=texto[5]
  if escolha3=="+":
    resultado=resultado+a
  elif escolha3=="-":
    resultado=resultado-a
  elif escolha3=="/":
    resultado=resultado/a
  elif escolha3=="x":
    resultado=resultado*a
  elif escolha3=="^":
    resultado=resultado**a
if len(texto)>=9:
  b=float(str(texto[8]).replace(",", "."))
  escolha4=texto[7]
  if escolha4=="+":
    resultado=resultado+b
  elif escolha4=="-":
    resultado=resultado-b
  elif escolha4=="/":
    resultado=resultado/b
  elif escolha4=="x":
    resultado=resultado*b
  elif escolha4=="^":
    resultado=resultado**b

resultado=f"{resultado:_.2f}"
resultado=resultado.replace(".", ",").replace("_", ".") #As linhas 22 e 23 fazem que numeros grandes estejam escritos de acordo com a escrita de numeros brasileira

resultado_str=resultado[-3:]#os codigos desta linha até a 28 servem para retirar o ",00" do final se o numero for inteiro
if resultado_str==",00":
  resultado_str_cplt=str(resultado)
  resultado=resultado_str_cplt.replace(resultado_str, " ")

x=f"{x:_.2f}" #os codigos desta linha até a 35 servem para retirar o ",00" do final se o numero for inteiro
x=x.replace(".", ",").replace("_", ".")
x_str=x[-3:]
if x_str==",00":
  x_str_cplt=str(x)
  x=x_str_cplt.replace(x_str, " ")

y=f"{y:_.2f}" #os codigos desta linha até a 42 servem para retirar o ",00" do final se o numero for inteiro
y=y.replace(".", ",").replace("_", ".")
y_str=y[-3:]
if y_str==",00":
  y_str_cplt=str(y)
  y=y_str_cplt.replace(y_str, " ")



if len(texto)<=3:
  print(f"{x} {escolha1} {y} = {resultado}") #Mostra os números escolhidos a operação e o resultado final
elif len(texto)<=5:
  z=f"{z:_.2f}" #os codigos desta linha até a 42 servem para retirar o ",00" do final se o numero for inteiro
  z=z.replace(".", ",").replace("_", ".")
  z_str=z[-3:]
  if z_str==",00":
    z_str_cplt=str(z)
    z=z_str_cplt.replace(z_str, " ")
  print(f"{x} {escolha1} {y} {escolha2} {z} = {resultado}")
elif len(texto)<=7:
  a=f"{a:_.2f}" #os codigos desta linha até a 42 servem para retirar o ",00" do final se o numero for inteiro
  a=a.replace(".", ",").replace("_", ".")
  a_str=a[-3:]
  if a_str==",00":
    a_str_cplt=str(a)
    a=a_str_cplt.replace(a_str, " ")
  print(f"{x} {escolha1} {y} {escolha2} {z} {escolha3} {a} = {resultado}")
elif len(texto)<=9:
  b=f"{b:_.2f}" #os codigos desta linha até a 42 servem para retirar o ",00" do final se o numero for inteiro
  b=b.replace(".", ",").replace("_", ".")
  b_str=b[-3:]
  if b_str==",00":
    b_str_cplt=str(b)
    b=b_str_cplt.replace(b_str, " ")
  print(f"{x} {escolha1} {y} {escolha2} {z} {escolha3} {a} {escolha4} {b} = {resultado}")
