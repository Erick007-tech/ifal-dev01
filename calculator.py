#escolher primeiro número
x=float(input("digite o primeiro numer: ")) 

#possibilita a escolha de operação
escolha=input("Escolha a operacão dessas operações: x, :, -, +, ^ ||| ")

#escolher segundo número
y=float(input("digite o segundo numero: "))

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
print(f"{x} {escolha} {y} = {resultado}") #Mostra os números escolhidos a operação e o resultado final
