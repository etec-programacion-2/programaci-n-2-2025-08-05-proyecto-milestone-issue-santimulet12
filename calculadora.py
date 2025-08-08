def calculadora(a,b):
    return a + b

if __name__ == "__main__":
    resultado = calculadora(int(input("escribe un numero: ")), int(input("escribe otro numero: ")))
    print(f"el resultado es {resultado}")