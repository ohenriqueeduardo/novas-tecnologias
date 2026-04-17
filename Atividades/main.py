from matrix import transpor_matriz

num_linhas = int(input("Insira o número de linhas da matriz: "))
num_colunas = int(input("Insira o número de colunas da matriz: "))

matriz = []
for i in range(num_linhas):
      linha = []
      for j in range(num_colunas):
         elemento = int(input(f"Insira o elemento da posição ({i}, {j}): "))
         linha.append(elemento)
      matriz.append(linha)

print("")
print("*" * 30)
print("Matriz original:")
print("")
for linha in matriz:
    print(linha)

print("")
print("*" * 30)
print("Matriz transposta: ")
print("")
matriz_transposta = transpor_matriz(matriz)
for linha in matriz_transposta:
    print(linha)