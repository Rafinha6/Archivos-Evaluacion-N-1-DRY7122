def verificar_tipo_acl(numero_acl):
    if 1 <= numero_acl <= 99:
        return "Estándar"
    elif 100 <= numero_acl <= 199:
        return "Extendida"
    else:
        return "no corresponde a ninguna ACL"

if __name__ == "__main__":
    try:
        numero_acl = int(input("Introduce el número de ACL IPv4: "))
        tipo_acl = verificar_tipo_acl(numero_acl)
        if tipo_acl != "no corresponde a ninguna ACL":
            print("El número {} corresponde a una ACL {}".format(numero_acl, tipo_acl))
        else:
            print("El número {} {}".format(numero_acl, tipo_acl))
    except ValueError:
        print("Error: Por favor, introduzca un valor válido.")
