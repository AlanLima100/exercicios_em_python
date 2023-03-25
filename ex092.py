#CRIE UM PROGRAMA QUE LEIA NOME, ANO DE NASCIMENTO E CARTEIRA DE TRABALHO E CADASRTE-OS (COM IDADE) EM UM DICIONÁRIO SE POR ACASO A CTPS (CARTEIRA DE TRABALHO PREVIDENCIA SOCIAL)
# FOR DIFERENTE DE ZERO, O DICIONÁRIO RECEBERÁ TAMBÉM O ANO DE CONTRATAÇÃO E O SALÁRIO. CALCULE E ACRESCENTE, ALÉM DA IDADE, COM QUANTOS ANOS A PESSOA VAI SE APOSENTAR.
from datetime import datetime
dados = dict()

dados["nome"] = str(input("Nome:"))
dados["ano"] = int(input("Ano de nacimento:"))
dados["idade"] = datetime.now().year - dados["ano"]
dados["carteira de trabalho"] = int(input("N° da Carteira de trabalho ( digite 0 (zero) caso não tenha):"))

if dados["carteira de trabalho"] != 0:
    dados["ano de contratação"] = int(input("Ano de contratação:"))
    dados["salario"] = float(input("Salário: R$"))
    dados["aposentadoria"] = dados["idade"] + ((dados["ano de contratação"] + 35) - datetime.now().year)

for k, v in dados.items():
    print(f"   - {k} e {v}")


# professor fez:

from datetime import datetime

dados = dict()
dados["nome"] = str(input("Name:"))
ano_nasc = int(input("Ano de Nascimento:"))
dados["idade"] = datetime.now().year - ano_nasc
dados["Carteira_trabalho"] = int(input("Carteira de Trabalho:"))
if dados["Carteira_trabalho"] != 0:
    dados["contratação"] = int(input("Ano de Contratação: "))
    dados["salário"] = float(input("Salário: R$"))
    dados["Aposentadoria"] = dados["idade"] + ((dados["contratação"] + 35) - datetime.now().year)
print("-=" * 30)
for k, v in dados.items():
    print(f"  - {k} tem o valor {v}")

print(datetime.today())
