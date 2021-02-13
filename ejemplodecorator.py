def mi_decorador(funcion):
    def nueva_funcion(a, b):
        print("Se va a llamar")
        c = funcion(a, b)
        print("Se ha llamado")
        return c
    return nueva_funcion

@mi_decorador
def suma(a, b):
    print("Entra en funcion suma")
    print(a+b)
    return a+b

suma(5,8)

# Se va a llamar
# Entra en funcion suma
# Se ha llamado