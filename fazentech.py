def busca_binaria(v, p, r, x):
    # condição de parada
    if p <= r:
        q = (p + r) // 2  # buscando o índice do meio do vetor
        if x > v[q]:
            return busca_binaria(v, q + 1, r, x)
        elif x < v[q]:
            return busca_binaria(v, p, q - 1, x)
        else:
            return q  # Encontrado

    return -1  # Não encontrado


vacas_ordenhadas = list(range(1, 5000))
vaca = 500
posicao = busca_binaria(vacas_ordenhadas, 0, len(vacas_ordenhadas) - 1, vaca)

if posicao >= 0:
    print("\033[1:32mA vaca %d foi ordenhada e se encontra na posição: %d.\033[m" % (vaca, posicao))
else:
    print("\033[1:31mA vaca NÃO foi ordenhada.\033[m")

print(vacas_ordenhadas)
