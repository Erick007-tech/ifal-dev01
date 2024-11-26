print("vamos ver se voce concorda... o jorge é feio?")
def escolha():
    print("s/n ")
    opcao=input("")
    if "S" in opcao.capitalize():
        print("concorda")
    else:
        print("discorda")
        escolha()
escolha()