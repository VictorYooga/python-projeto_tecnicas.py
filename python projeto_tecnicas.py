# Questão 1: Sequência de Fibonacci

def fibonacci_check(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    if b == num or num == 0:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

# Teste da função
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
print(fibonacci_check(numero))

# Questão 2: Verificação da letra 'a' em uma string

def count_a(string):
    count = string.lower().count('a')
    if count > 0:
        return f"A letra 'a' aparece {count} vez(es) na string."
    else:
        return "A letra 'a' não aparece na string."

# Teste da função
texto = input("Digite uma string para verificar a ocorrência da letra 'a': ")
print(count_a(texto))

# Questão 3: Cálculo da variável SOMA

INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K += 1
    SOMA += K

print(f"O valor final da variável SOMA é: {SOMA}")

# Questão 4: Completar sequências lógicas

sequencias = [
    [1, 3, 5, 7, 9],  # a) Próximo número é 9 (soma 2)
    [2, 4, 8, 16, 32, 64, 128],  # b) Próximo número é 128 (multiplica por 2)
    [0, 1, 4, 9, 16, 25, 36, 49],  # c) Próximo número é 49 (quadrados dos números naturais)
    [4, 16, 36, 64, 100],  # d) Próximo número é 100 (quadrados dos números pares)
    [1, 1, 2, 3, 5, 8, 13],  # e) Próximo número é 13 (soma dos dois anteriores - Fibonacci)
    [2, 10, 12, 16, 17, 18, 19, 20]  # f) Próximo número é 20 (sequência com padrão mais complexo)
]

for i, seq in enumerate(sequencias):
    print(f"{chr(97 + i)}) {', '.join(map(str, seq[:-1]))}, ___")
    print(f"   Resposta: {seq[-1]}")

# Questão 5: Problema dos interruptores e lâmpadas

print("\nSolução para o problema dos interruptores e lâmpadas:")
print("1. Ligue o primeiro interruptor e deixe-o ligado por alguns minutos.")
print("2. Desligue o primeiro interruptor e ligue o segundo.")
print("3. Entre na primeira sala:")
print("   - Se a lâmpada estiver acesa, o segundo interruptor controla essa lâmpada.")
print("   - Se a lâmpada estiver apagada, mas quente, o primeiro interruptor controla essa lâmpada.")
print("   - Se a lâmpada estiver apagada e fria, o terceiro interruptor controla essa lâmpada.")
print("4. Com essa informação, você já sabe qual interruptor controla duas das três lâmpadas.")
print("5. Entre na segunda sala para confirmar qual dos dois interruptores restantes controla a lâmpada dessa sala.")
print("6. Por eliminação, você saberá qual interruptor controla a lâmpada da terceira sala.")