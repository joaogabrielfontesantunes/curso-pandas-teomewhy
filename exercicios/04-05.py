# Selecione a primeira transação diária de cada cliente.

# %%
import pandas as pd
df = pd.read_csv("../arquivos/transacoes.csv", sep=";")
# %%
df["DtCriacao"] = pd.to_datetime(df["DtCriacao"])
df["Dia"] = df["DtCriacao"].dt.date
df = df.sort_values(by=["IdCliente", "DtCriacao"])
df["Ordem"] = df.groupby(["IdCliente", "Dia"]).cumcount() + 1
filtro = df["Ordem"] == 1
# %%
df[filtro].drop(columns=["Ordem", "Dia"])
# %%
