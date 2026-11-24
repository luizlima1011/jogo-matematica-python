import random


def gerar_desafio(nivel):
    """Gera uma pergunta matemática conforme o nível de dificuldade escolhido."""
    if nivel == 1:
        # Nível 1: Expressões numéricas básicas (prioridade de operações)
        a = random.randint(2, 10)
        b = random.randint(2, 10)
        c = random.randint(1, 15)
        pergunta = f"Quanto é {c} + {a} x {b}?"
        resposta_correta = c + (a * b)

    elif nivel == 2:
        # Nível 2: Múltiplos e Divisores
        divisor = random.randint(3, 12)
        quociente = random.randint(4, 15)
        numero = divisor * quociente
        pergunta = f"Qual é o resultado da divisão exata de {numero} por {divisor}?"
        resposta_correta = quociente

    else:
        # Nível 3: Fração de uma quantidade (ex: 2/5 de 30)
        denominador = random.choice([2, 3, 4, 5, 10])
        numerador = random.randint(1, denominador - 1)
        total = denominador * random.randint(3, 12)
        pergunta = f"Quanto vale {numerador}/{denominador} de {total}?"
        resposta_correta = (total // denominador) * numerador

    return pergunta, resposta_correta


def jogar():
    print("=" * 50)
    print("   DESAFIO MATEMÁTICO - 6º ANO (MODO CONSOLE)")
    print("=" * 50)
    print("Escolha o nível de dificuldade:")
    print("1 - Iniciante (Expressões Numéricas)")
    print("2 - Intermediário (Divisão e Múltiplos)")
    print("3 - Avançado (Frações de Quantidades)")

    # Validação da escolha de nível
    while True:
        try:
            nivel = int(input("\nDigite o nível (1, 2 ou 3): "))
            if nivel in [1, 2, 3]:
                break
            print("Opção inválida. Escolha 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")

    pontuacao = 0
    total_rodadas = 5

    for rodada in range(1, total_rodadas + 1):
        print(f"\n--- Rodada {rodada} de {total_rodadas} ---")
        pergunta, resposta_correta = gerar_desafio(nivel)
        print(pergunta)

        # Tratamento de exceção para evitar erro caso o aluno digite texto
        while True:
            try:
                palpite = int(input("Sua resposta: "))
                break
            except ValueError:
                print("Por favor, digite apenas um número inteiro.")

        if palpite == resposta_correta:
            print("Correto! +20 pontos.")
            pontuacao += 20
        else:
            print(f"Incorreto. A resposta certa era {resposta_correta}.")

    print("\n" + "=" * 50)
    print(f"FIM DE JOGO! Pontuação final: {pontuacao} de 100 pontos.")
    if pontuacao == 100:
        print("Desempenho excelente! Você dominou o conteúdo.")
    elif pontuacao >= 60:
        print("Bom trabalho! Continue praticando.")
    else:
        print("Que tal revisar o conteúdo e tentar novamente?")
    print("=" * 50)


if __name__ == "__main__":
    jogar()
