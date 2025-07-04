import random

# Lista para armazenar o ranking
ranking = []

def jogar():
    nome = input("Qual é o seu nome? ").strip()
    numero_misterioso = random.randint(1, 100)
    tentativas_restantes = 3
    pontos = 0

    print(f"\nBem-vindo, {nome}! Você tem 3 tentativas para adivinhar o número misterioso de 1 a 100.")

    while tentativas_restantes > 0:
        try:
            palpite = int(input(f"Tentativa {4 - tentativas_restantes}: Qual é o seu palpite? "))
            
            if palpite < 1 or palpite > 100:
                print("Por favor, digite um número entre 1 e 100.")
                continue

            if palpite == numero_misterioso:
                print(f"Parabéns, {nome}! Você acertou o número misterioso!")
                pontos = 4 - tentativas_restantes  # A pontuação é baseada nas tentativas restantes
                break
            elif palpite < numero_misterioso:
                print("O número misterioso é MAIOR.")
            else:
                print("O número misterioso é MENOR.")
                
            tentativas_restantes -= 1

            if tentativas_restantes == 0:
                print(f"Você perdeu! O número misterioso era {numero_misterioso}.")

        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")

    # Adiciona o nome e a pontuação ao ranking
    ranking.append({"nome": nome, "pontos": pontos})

    print(f"\n{nome}, você fez {pontos} ponto(s).")
    
    # Exibe o ranking
    print("\n=== Ranking Atual ===")
    ranking_sorted = sorted(ranking, key=lambda x: x['pontos'], reverse=True)
    for i, jogador in enumerate(ranking_sorted, start=1):
        print(f"{i}. {jogador['nome']} - {jogador['pontos']} ponto(s)")

def menu():
    while True:
        print("\n=== Menu do Jogo Misterioso ===")
        print("1. Jogar")
        print("2. Sair")
        
        opcao = input("Escolha uma opção (1 ou 2): ").strip()
        
        if opcao == '1':
            jogar()
        elif opcao == '2':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Inicia o menu
menu()
