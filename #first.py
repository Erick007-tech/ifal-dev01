#frist
beleza=int(input("Dê um numero para a beleza de Jorge: "))
fome=int(input("Dê um numero para a fome de Jorge: "))

if beleza<=0:
  print("jorge é feio")
elif beleza<=1 or beleza>=9:
  print("jorge é bonitinho")
elif beleza>=10:
  print("jorge é bonito")

if fome<=0:
  print("jorge está cheio")
elif fome<=1 or fome<=9:
  print("jorge está com fominha")
elif fome>=10:
  print("jorge esta faminto")


print( )

print(fome)
print(beleza)

