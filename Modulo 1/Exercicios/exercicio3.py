convite_codigo= "vip"
convite= input("digite o codigo do convite: ").strip().lower()
if convite_codigo == convite:
    print("convite valido")
else:
    print("convite invalido")