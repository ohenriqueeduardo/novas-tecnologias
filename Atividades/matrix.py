def transpor_matriz(matriz):
    transposta = []
    for i in range(len(matriz[0])):
        linha_transposta = []
        for j in range(len(matriz)):
            linha_transposta.append(matriz[j][i])
        transposta.append(linha_transposta)
    return transposta