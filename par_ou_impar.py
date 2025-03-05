import random  # Importa o módulo 'random' para gerar números aleatórios.

def par_ou_impar():
    """
    Jogo de par ou ímpar contra o computador.
    """

    while True:  # Inicia um loop infinito que só será quebrado quando o jogador decidir sair.
        escolha = input("Escolha par, ímpar ou sair: ").lower()  # Solicita a escolha do jogador (par, ímpar ou sair) e converte a entrada para minúsculas.

        if escolha == "sair":  # Verifica se o jogador escolheu "sair".
            print("Saindo do jogo...")  # Imprime uma mensagem indicando que o jogo está sendo encerrado.
            break  # Sai do loop 'while True', encerrando o jogo.
        elif escolha not in ("par", "ímpar", "impar"):  # Verifica se a escolha do jogador é inválida (não é "par", "ímpar" ou "sair").
            print("Escolha inválida. Digite par, ímpar ou sair.")  # Imprime uma mensagem de erro informando que a escolha é inválida.
            continue  # Volta para o início do loop 'while True', solicitando uma nova escolha.

        if escolha == "par":  # Verifica se o jogador escolheu "par".
            computador_escolha = "ímpar"  # Se o jogador escolheu "par", o computador escolhe "ímpar".
            print("Você escolheu par, o computador escolheu ímpar.")  # Imprime uma mensagem informando as escolhas.
        else:  # Se o jogador não escolheu "par", significa que ele escolheu "ímpar" (ou "impar", já que estamos tratando com lower case).
            computador_escolha = "par"  # Se o jogador escolheu "ímpar", o computador escolhe "par".
            print("Você escolheu ímpar, o computador escolheu par.")  # Imprime uma mensagem informando as escolhas.
            
        if escolha == "impar": #verifica se a escolha foi "impar", se sim, muda para "ímpar" para o correto funcionamento do código.
            escolha = "ímpar"

        while True:  # Inicia um loop para garantir que o jogador digite um número válido.
            try:  # Inicia um bloco 'try-except' para lidar com possíveis erros de entrada.
                numero_usuario = int(input("Digite um número de 0 a 5: "))  # Solicita que o jogador digite um número inteiro entre 0 e 5 e tenta convertê-lo para inteiro.
                if 0 <= numero_usuario <= 5:  # Verifica se o número digitado está dentro do intervalo permitido (0 a 5).
                    break  # Se o número estiver no intervalo, sai do loop 'while True'.
                else:  # Se o número estiver fora do intervalo.
                    print("Número fora do intervalo permitido (0 a 5).")  # Imprime uma mensagem de erro.
            except ValueError:  # Se o jogador digitar algo que não pode ser convertido para inteiro, o erro ValueError é capturado.
                print("Entrada inválida. Digite um número inteiro.")  # Imprime uma mensagem de erro.

        numero_computador = random.randint(0, 5)  # O computador escolhe um número aleatório entre 0 e 5 (inclusive).
        print(f"O computador escolheu: {numero_computador}")  # Imprime o número escolhido pelo computador.

        soma = numero_usuario + numero_computador  # Calcula a soma dos números escolhidos pelo jogador e pelo computador.
        print(f"A soma é: {soma}")  # Imprime o valor da soma.

        if soma % 2 == 0:  # Verifica se a soma é par (resto da divisão por 2 é 0).
            resultado = "par"  # Se for par, o resultado é "par".
        else:  # Se não for par, é ímpar.
            resultado = "ímpar"  # Se for ímpar, o resultado é "ímpar".

        if resultado == escolha:  # Compara o resultado (par ou ímpar) com a escolha do jogador.
            print("Você ganhou!")  # Se o resultado for igual à escolha do jogador, o jogador ganhou.
        else:  # Caso contrário.
            print("O computador ganhou!")  # O computador ganhou.

        print("-" * 20)  # Imprime uma linha de separação para melhorar a legibilidade.

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente.
    par_ou_impar()  # Se sim, chama a função 'par_ou_impar' para iniciar o jogo.
