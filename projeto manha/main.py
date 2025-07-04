import random

# Gera um número aleatório entre 1 e 100
numero_misterioso = random.randint(1, 100)

print("Bem-vindo ao jogo do Número Misterioso!")
print("Você tem 3 tentativas para adivinhar um número de 1 a 100.")

# O jogador tem 3 tentativas
for tentativa in range(1, 4):
    try:
        palpite = int(input(f"Tentativa {tentativa}: Qual é o seu palpite? "))
        
        if palpite < 1 or palpite > 100:
            print("Por favor, insira um número entre 1 e 100.")
            continue
        
        if palpite == numero_misterioso:
            print("Parabéns! Você acertou o número misterioso!")
            break
        elif palpite < numero_misterioso:
            print("O número misterioso é MAIOR que isso.")
        else:
            print("O número misterioso é MENOR que isso.")
        
        if tentativa == 3:
            print(f"Fim de jogo! O número misterioso era {numero_misterioso}.")
    
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

