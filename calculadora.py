# Declara as variáveis numéricas
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Configura a lógica das operações
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# Verifica se a divisão é possível
if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Indefinida (não é possível dividir por zero)"

# Exibe os resultados
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
