from excecao import ExcecionNumeroMuyLargo

try:
    nota = int(input("Digite uma nota: "))
    print("Nota:", nota)

    if nota > 100:
        raise ExcecionNumeroMuyLargo("Desculpe, não aceitamos esse valor.")

except ValueError:
    print("Erro, digite um número inteiro.")

except ExcecionNumeroMuyLargo:
    print("Insira um número menor que 101!")





