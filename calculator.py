#escolher os numeros para operação
x=int(input("digite o primeiro numer: ")) 
y=int(input("digite o segundo numero: "))


#possibilita a escolha de operação
escolha=input("Escolha a operacão dessas operações: x, :, -, + ||| ")


#exculta a operação de acordo com a escolha
if escolha=="x":
  print(f"{x} x {y} = {x*y}")
elif escolha=="/":
  print(f"{x} : {y} = {x/y}")
elif escolha=="+":
  print(f"{x} + {y} = {x+y}")
elif escolha=="-":
  print(f"{x} - {y} = {x-y}")
