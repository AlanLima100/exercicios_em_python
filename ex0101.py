# CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMA VOTO() QUE VAI RECEBER COMO PARÂMETRO O ANO DE NASCIMENTO DE UMA PESSOA, RETORNANDO UM VALOR LITERAL INDICANDO SE UMA PESSOA TEM

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f"com idade {idade} anos: NÂO VOTA"
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL"
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"


#PROGRAMA PRINCIPAL
ano = int(input("Digite o ano de nascimento?: "))
print(voto(ano))
