# Qual a média de transações / dia?

# %%
import pandas as pd
df = pd.read_csv("../arquivos/transacoes.csv", sep=";")
# %%
df["Dia"] = pd.to_datetime(df["DtCriacao"]).dt.date
qtde_de_dias = len(df["Dia"].unique().tolist())
qtde_de_transacoes = df.shape[0]
media = round(qtde_de_transacoes / qtde_de_dias, 2)
# %%
print(f"A média de transações por dia é: {media}")
# %%