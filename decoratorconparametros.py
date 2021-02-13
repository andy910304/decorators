def mi_decorador(arg):
    def decorador_real(funcion):
        def nueva_funcion(a, b):
            print(arg)
            c = funcion(a, b)
            print(arg)
            return c
        return nueva_funcion
    return decorador_real

@mi_decorador("Imprimer esto antes y después")
def suma(a, b):
    print("Entra en funcion suma")
    print(a+b)
    return a + b

suma(5,8)
# Imprimer esto antes y después
# Entra en funcion suma
# Imprimer esto antes y después