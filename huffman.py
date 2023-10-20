from collections import Counter

class NoHuffman:
    def __init__(self, valor, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita

    def __str__(self):
        return f'{self.valor}'

def frequencias(texto):
    return Counter(texto)

def constroi_arvore(frequencias):
    nos = [NoHuffman(valor=freq) for freq in frequencias]
    while len(nos) > 1:
        nos = sorted(nos, key=lambda no: no.valor)
        esquerda = nos.pop(0)
        direita = nos.pop(0)
        novo_no = NoHuffman(valor=esquerda.valor + direita.valor, esquerda=esquerda, direita=direita)
        nos.append(novo_no)
    return nos[0]

def gera_codigos(arvore, prefixo='', codigos={}):
    if arvore:
        if not arvore.esquerda and not arvore.direita:
            codigos[arvore.valor] = prefixo
        gera_codigos(arvore.esquerda, prefixo + '0', codigos)
        gera_codigos(arvore.direita, prefixo + '1', codigos)
    return codigos

def huffman_codifica(texto):
    freq = frequencias(texto)
    arvore = constroi_arvore(freq)
    codigos = gera_codigos(arvore)
    return codigos

def main():
    texto = input("Digite uma string: ")

    codigos = huffman_codifica(texto)
    print("Tabela de códigos de Huffman:")
    for char, codigo in codigos.items():
        print(f"{char}: {codigo}")

    sequencia_binaria = ''.join(codigos[caractere] for caractere in texto)
    print(f"Sequência binária resultante: {sequencia_binaria}")


if __name__ == '__main__':
    main()
