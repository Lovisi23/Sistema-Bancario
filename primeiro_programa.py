def exibir_mensagem():
    print("Ola, bom dia!")

def exibir_mensagem2(nome):
    print(f'Prazer {nome}!')

def soma(a,b):
    return a + b

def exibir_resultado(a, b, function):
    resultado = function(a,b)
    print(f"O resultado é = {resultado}")

exibir_resultado(3, 4, soma)

v = float(input())

print(f"v = {v}")