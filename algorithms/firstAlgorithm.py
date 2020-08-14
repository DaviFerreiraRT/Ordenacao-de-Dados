soma=0
valor(float(input("Digite um 'valor'para 0 ou para parar: ")))

while valor !=0:

    soma+=valor
    print(f"Soma atual: {soma}")
    valor=float(input("Digite um 'valor' ou 0 para parar:" ))

        if soma>10:
            print("Soma é maior do que 10")
        elif soma<10:
            print("Soma é menor do que 10")
            else:
                print("Soma é igual a 10")