# Quantas transações ocorreram no dia 2025-02-01?

# %%
import pandas as pd
df = pd.read_csv("../arquivos/transacoes.csv", sep=";")
# %%
df["DtCriacao"] = pd.to_datetime(df["DtCriacao"])
filtro = df["DtCriacao"].dt.normalize() == "2025-02-01"
qnt_filtro = df[filtro].shape[0]
# %%
print(f"Ocorreram {qnt_filtro} transações no dia 2025-02-01")
# %%
