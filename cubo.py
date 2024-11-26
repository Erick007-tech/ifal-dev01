def line():
    x=int(input("tamanho da linha: "))
    print("🎹"*x)

def pilar():
    x=int(input("tamanho do pilar: "))
    while x>0:
        print("🛢️")
        x -= 1

def cubo():
    x=int(input("tamanho do cubo: "))
    y=x
    while x>0:
        print("🟧"*y)
        x-=1

escolha=input("Escolha: linha, pilar ou cubo: ")
if escolha.capitalize()=="Pilar":
    pilar()
elif escolha.capitalize()=="Linha":
    line()
elif escolha.capitalize()=="Cubo":
    cubo()
else:
    print("erro😐")