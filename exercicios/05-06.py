# Como podemos calcular as estatísticas descritivas dos pontos das transações de cada usuário?

# %%
import pandas as pd
df = pd.read_csv("../arquivos/transacoes.csv", sep=";")
# %%
df.groupby("IdCliente")["QtdePontos"].describe().reset_index()
# %%
