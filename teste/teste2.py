entrada_usuario = input("Informe um número inteiro: ")

while not entrada_usuario.isdigit():
    print('Digite apenas números inteiros!')
    entrada_usuario = input("Informe um número: ")

numero_informado = int(entrada_usuario)

def verificar_entrada(numero):
    termo_anterior, termo_atual = 0, 1
    
    while termo_atual < numero:
        termo_anterior, termo_atual = termo_atual, termo_anterior + termo_atual

    if termo_atual == numero:
        return f"{numero} faz parte da sequência de Fibonacci."
    else:
        return f"{numero} não faz parte da sequência de Fibonacci."

resultado = verificar_entrada(numero_informado)
print(resultado)
