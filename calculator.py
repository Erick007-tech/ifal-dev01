#definir a expressão que ira ser feita
texto=input("digite um calculo. ex: (1 + 1): ") 

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

escolha=texto[1]

#execulta a operação de acordo com a escolha
if escolha=="+":
  resultado=x+y
elif escolha=="-":
  resultado=x-y
elif escolha=="/":
  resultado=x/y
elif escolha=="x":
  resultado=x*y
elif escolha=="^":
  resultado=x**y

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

print(f"{x} {escolha} {y} = {resultado}") #Mostra os números escolhidos a operação e o resultado final
