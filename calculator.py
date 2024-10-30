#escolher primeiro número
x=float(input("digite o primeiro numer: ").replace(",", ".")) 

#possibilita a escolha de operação
escolha=input("Escolha a operacão dessas operações: x, :, -, +, ^ ||| ")

#escolher segundo número
y=float(input("digite o segundo numero: ").replace(",", "."))

#execulta a operação de acordo com a escolha
if escolha=="x":
  resultado=x*y
elif escolha=="/":
  resultado=x/y
elif escolha=="+":
  resultado=x+y
elif escolha=="-":
  resultado=x-y
elif escolha=="^":
  resultado=x**y

resultado=f"{resultado:_.2f}"
resultado=resultado.replace(".", ",").replace("_", ".") #As linhas 22 e 23 fazem que numeros grandes estejam escritos de acordo com a escrita de numeros brasileira

resultado_str=resultado[-3:]#os codigos desta linha até a 28 servem para retirar o ",00" do final se o numero for inteiro
if resultado_str==",00":
  resultado_str_cplt=str(resultado)
  resultado=int(resultado_str_cplt.replace(resultado_str, " "))

x=f"{x:_.2f}" #os codigos desta linha até a 35 servem para retirar o ",00" do final se o numero for inteiro
x=x.replace(".", ",").replace("_", ".")
x_str=x[-3:]
if x_str==",00":
  x_str_cplt=str(x)
  x=int(x_str_cplt.replace(x_str, " "))

y=f"{y:_.2f}" #os codigos desta linha até a 42 servem para retirar o ",00" do final se o numero for inteiro
y=y.replace(".", ",").replace("_", ".")
y_str=y[-3:]
if y_str==",00":
  y_str_cplt=str(y)
  y=int(y_str_cplt.replace(y_str, " "))

print(f"{x} {escolha} {y} = {resultado}") #Mostra os números escolhidos a operação e o resultado final
