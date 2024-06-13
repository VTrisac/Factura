artic1 = input("Primer artículo: ")
partic1 = eval(input("Precio: "))
artic2 = input("Segundo artículo: ")
partic2 = eval(input("Precio: "))
artic3 = input("Tercer artículo: ")
partic3 = eval(input("Precio: "))
print()
print("factura".upper().center(80, "-"))
print(artic1.title().ljust(73, ".") + str(partic1).zfill(6) + "€")
print(artic2.title().ljust(73, ".") + str(partic2).zfill(6) + "€")
print(artic3.title().ljust(73, ".") + str(partic3).zfill(6) + "€")
print("-".center(80, "-"))
base = partic1 + partic2 + partic3
iva = base * 0.21
total = base + iva

txtbase = str(base)
txtbase = txtbase[:txtbase.find(".") + 3]

txtiva = str(iva)
txtiva = txtiva[:txtiva.find(".") + 3]

txttotal = str(total)
txttotal = txttotal[:txttotal.find(".") + 3]

print("Precio base: ".rjust(73) + txtbase.zfill(6) + "€")
print("IVA: ".rjust(73) + txtiva.zfill(6) + "€")
print("TOTAL A PAGAR: ".rjust(73) + txttotal.zfill(6) + "€")