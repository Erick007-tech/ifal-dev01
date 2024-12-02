print("-LANCHES-\n1-Coxinha\n2-Pastel\n3-X-burguer\n4-Batata frita\n5-Pizza\n ")
print("-SALGADINHOS-\n1-Gula\n2-Cheetos\n3-Fandangos\n ")
print("-BEBIDAS-\n1-Coca-cola\n2-Pepsi\n3-Soda\n4-fanta\n5-Coca 0\n ")
x=input("escolha uma ou mais comidas\n(Exemplo: coxinha, coca-cola)\n")


salgados=[]


x=x.replace(",", "")

escolha=[
    {"nome": "coxinha", "calorias":2.5, "fibras":0.1, "sódio":0.2, "acucares":0.05},# juukfoog
    {"nome": "pastel", "calorias":3.5, "fibras":0.05, "sódio":0.1, "acucares":0.2},
    {"nome": "x-burguer", "calorias":2.8, "fibras":0.05, "sódio":0.2, "acucares":0.3},
    {"nome": "batata frita", "calorias":5, "fibras":0.05, "sódio":0.3, "acucares":0.4},
    {"nome": "pizza", "calorias":2.8, "fibras":0.05, "sódio":0.15, "acucares":0.15},
    {"nome": "gula", "calorias":5, "fibras":0.1, "sódio":0.025, "acucares":0.03},
    {"nome": "cheatos", "calorias":5.3, "fibras":0.1, "sódio":0.025, "acucares":0.03},
    {"nome": "fandangos", "calorias":5, "fibras":0.1, "sódio":0.025, "acucares":0.05},
    {"nome": "coca-cola", "calorias":0.42, "fibras":0, "sódio":0.10, "acucares":0.001},#bebidas
    {"nome": "pepsi", "calorias":0.42, "fibras":0, "sódio":0.10, "acucares":0.1},
    {"nome": "soda", "calorias":0.5, "fibras":0, "sódio":0.10, "acucares":0.001},
    {"nome": "fanta", "calorias":0.45, "fibras":0, "sódio":0.10, "acucares":0.001},
    {"nome": "coca 0", "calorias":0, "fibras":0, "sódio":0, "acucares":0.001}
    
]


if "coxinha" in x.lower():
    gramas=input("Você esccolheu coxinha certo?\nQuanto de coxinha ex:(300g) ").replace("g", "")
    gramas_cox=escolha[0]["calorias"]*float(gramas)
    fibras_cox=escolha[0]["fibras"]*float(gramas)
    sodio_cox=escolha[0]["sódio"]*float(gramas)
    acucares_cox=escolha[0]["acucares"]*float(gramas)
    print(escolha[0]["nome"], f"calorias: {gramas_cox}, fibras: {fibras_cox}, sódio: {sodio_cox}, acucares: {acucares_cox}")

if "pastel" in x.lower():
    gramas=input("Você esccolheu pastel certo?\nQuanto de pastel ex:(300g) ").replace("g", "")
    gramas_pas=escolha[1]["calorias"]*float(gramas)
    fibras_pas=escolha[1]["fibras"]*float(gramas)
    sodio_pas=escolha[1]["sódio"]*float(gramas)
    acucares_pas=escolha[1]["acucares"]*float(gramas)
    print(escolha[1]["nome"], f"calorias: {gramas_pas}, fibras: {fibras_pas}, sódio: {sodio_pas}, acucares: {acucares_pas}")

if "x-burguer" in x.lower():
    gramas=input("Você esccolheu x-burguer certo?\nQuanto de x-burguer ex:(300g) ").replace("g", "")
    gramas_x=escolha[2]["calorias"]*float(gramas)
    fibras_x=escolha[2]["fibras"]*float(gramas)
    sodio_x=escolha[2]["sódio"]*float(gramas)
    acucares_x=escolha[2]["acucares"]*float(gramas)
    print(escolha[2]["nome"], f"calorias: {gramas_x}, fibras: {fibras_x}, sódio: {sodio_x}, acucares: {acucares_x}")
    
if "batata frita" in x.lower():
    gramas=input("Você esccolheu batata frita certo?\nQuanto de batata frita ex:(300g) ").replace("g", "")
    gramas_bat=escolha[3]["calorias"]*float(gramas)
    fibras_bat=escolha[3]["fibras"]*float(gramas)
    sodio_bat=escolha[3]["sódio"]*float(gramas)
    acucares_bat=escolha[3]["acucares"]*float(gramas)
    print(escolha[3]["nome"], f"calorias: {gramas_bat}, fibras: {fibras_bat}, sódio: {sodio_bat}, acucares: {acucares_bat}")


if "pizza" in x.lower():
    gramas=input("Você esccolheu piza certo?\nQuanto de piza ex:(300g) ").replace("g", "")
    gramas_piz=escolha[4]["calorias"]*float(gramas)
    fibras_piz=escolha[4]["fibras"]*float(gramas)
    sodio_piz=escolha[4]["sódio"]*float(gramas)
    acucares_piz=escolha[4]["acucares"]*float(gramas)
    print(escolha[4]["nome"], f"calorias: {gramas_piz}, fibras: {fibras_piz}, sódio: {sodio_piz}, acucares: {acucares_piz}")

if "gula" in x.lower():
    gramas=input("Você esccolheu gula certo?\nQuanto de gula ex:(300g) ").replace("g", "")
    gramas_gu=escolha[5]["calorias"]*float(gramas)
    fibras_gu=escolha[5]["fibras"]*float(gramas)
    sodio_gu=escolha[5]["sódio"]*float(gramas)
    acucares_gu=escolha[5]["acucares"]*float(gramas)
    print(escolha[5]["nome"], f"calorias: {gramas_gu}, fibras: {fibras_gu}, sódio:{sodio_gu}, acucares: {acucares_gu}")

if "cheetos" in x.lower():
    gramas=input("Você esccolheu cheetos certo?\nQuanto de cheetos ex:(300g) ").replace("g", "")
    gramas_ch=escolha[6]["calorias"]*float(gramas)
    fibras_ch=escolha[6]["fibras"]*float(gramas)
    sodio_ch=escolha[6]["sódio"]*float(gramas)
    acucares_ch=escolha[6]["acucares"]*float(gramas)
    print(escolha[6]["nome"], f"calorias: {gramas_ch}, fibras: {fibras_ch}, sódio:{sodio_ch}, acucares: {acucares_ch}")

if "fandango" in x.lower():
    gramas=input("Você esccolheu fandango certo?\nQuanto de fandangos ex:(300g) ").replace("g", "")
    gramas_fan=escolha[7]["calorias"]*float(gramas)
    fibras_fan=escolha[7]["fibras"]*float(gramas)
    sodio_fan=escolha[7]["sódio"]*float(gramas)
    acucares_fan=escolha[7]["acucares"]*float(gramas)
    print(escolha[7]["nome"], f"caloias: {gramas_fan}, fibras: {fibras_fan}, sódio:{sodio_fan}, acucares: {acucares_fan}")

if "coca-cola" in x.lower():
    ml=input("Você esccolheu coca-cola certo?\nQuanto de coca-cola ex:(100ml) ").replace("ml", "")
    ml_co=escolha[8]["calorias"]*float(ml)
    fibras_co=escolha[8]["fibras"]*float(ml)
    sodio_co=escolha[8]["sódio"]*float(ml)
    acucares_co=escolha[8]["acucares"]*float(ml)
    print(escolha[8]["nome"], f"calorias: {ml_co}, fibras: {fibras_co}, sódio:{sodio_co}, acucares: {acucares_co}")

if "pepsi" in x.lower():
    ml=input("Você escolheu pepsi certo?\nQuanto de pepsi ex:(100ml) ").replace("ml", "")
    ml_pe=escolha[9]["calorias"]*float(ml)
    fibras_pe=escolha[9]["fibras"]*float(ml)
    sodio_pe=escolha[9]["sódio"]*float(ml)
    acucares_pe=escolha[9]["acucares"]*float(ml)
    print(escolha[9]["nome"], f"calorias: {ml_pe}, fibras: {fibras_pe}, sódio:{sodio_pe}, acucares: {acucares_pe}")

if "soda" in x.lower():
    ml=input("Você esccolheu soda certo?\nQuanto de soda ex:(100ml) ").replace("ml", "")
    ml_so=escolha[10]["calorias"]*float(ml)
    fibras_so=escolha[10]["fibras"]*float(ml)
    sodio_so=escolha[10]["sódio"]*float(ml)
    acucares_so=escolha[10]["acucares"]*float(ml)
    print(escolha[10]["nome"], f"calorias: {ml_so}, fibras: {fibras_so}, sódio:{sodio_so}, acucares: {acucares_so}")

if "fanta" in x.lower():
    ml=input("Você esccolheu fanta certo?\nQuanto de fanta ex:(100ml) ").replace("ml", "")
    ml_fa=escolha[11]["calorias"]*float(ml)
    fibras_fa=escolha[10]["fibras"]*float(ml)
    sodio_fa=escolha[10]["sódio"]*float(ml)
    acucares_fa=escolha[10]["acucares"]*float(ml)
    print(escolha[11]["nome"], f"calorias: {ml_fa}, fibras: {fibras_fa}, sódio:{sodio_fa}, acucares: {acucares_fa}")

if "coca 0" in x.lower():
    ml=input("Você esccolheu coca 0 certo?\nQuanto de coca 0 ex:(100ml) ").replace("ml", "")
    ml_co0=escolha[12]["calorias"]*float(ml)
    fibras_co0=escolha[10]["fibras"]*float(ml)
    sodio_co0=escolha[10]["sódio"]*float(ml)
    acucares_co0=escolha[10]["acucares"]*float(ml)
    print(escolha[12]["nome"], f"calorias: {ml_co0}, fibras: {fibras_co0}, sódio:{sodio_co0}, acucares: {acucares_co0}")