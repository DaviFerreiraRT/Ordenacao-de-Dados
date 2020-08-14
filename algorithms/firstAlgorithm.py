# Algoritmo de soma
soma = 0
valor = float(input("Digite um valor para somar ou 0 para parar: "))

while valor != 0:

    soma += valor
    print(f"Soma atual: {soma}")
    valor = float(input("Digite um valor para somar ou 0 para parar:"))
if soma > 10:

    print("O resultado da soma foi acima de 10, a soma foi : ", soma)
elif soma < 10:
    print("O resultado da soma foi abaixo de 10, a soma foi: ", soma)
else:
    print("Soma é igual a 10")
