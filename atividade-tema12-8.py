# Inicializa a soma dos números primos
primos_soma = 0

# Loop para iterar sobre os números de 2 a 100
num = 2
while num <= 100:
    # Assume que o número é primo até que se prove o contrário
    primos = True

    # Verifica se o número é divisível por algum número entre 2 e a raiz quadrada do número
    divisor = 2
    while divisor * divisor <= num and primos:
        # Se o número for divisível por qualquer divisor, não é primo
        if num % divisor == 0:
            primos= False
        # Incrementa o divisor para testar o próximo número
        divisor += 1

    # Se o número for primo, adiciona à soma dos números primos
    if primos:
        primos_soma += num

    # Incrementa o número para testar o próximo número na sequência
    num += 1

# Imprime a soma de todos os números primos entre 1 e 100
print(f"A soma de todos os números primos entre 1 e 100 é:", primos_soma)

