# Qual o saldo de pontos do cliente na 10a posição (sem ordenar) do arquivo clientes.csv ?

# %%
import pandas as pd
df = pd.read_csv("../arquivos/clientes.csv", sep=";")
# %%
saldo_pontos = int(df.iloc[9]["qtdePontos"])
# %%
print(f"O saldo de pontos desse cliente é {saldo_pontos}")
# %%
