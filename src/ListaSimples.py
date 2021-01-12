teste = []
lista = [15, 21, 22, 45]
teste.insert(1, 5)
teste.insert(2, 10)
teste.insert(3, 2)
print(lista)
teste.extend(lista)
print(teste)
teste.reverse()
print(teste)
teste.sort()
for a in teste:
    print("Valores da lista:", a)

print("Total de elementos da lista:", len(teste))
