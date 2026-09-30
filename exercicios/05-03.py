# Qual usuário teve maior quantidade de pontos debitados?

# %%
import pandas as pd
df1 = pd.read_csv("../arquivos/transacao_produto.csv", sep=";")
df2 = pd.read_csv("../arquivos/transacoes.csv", sep=";")
# %%
filtro = df1["vlProduto"] < 0
df1 = df1[filtro]
# %%
df = pd.merge(df1, df2, how="inner", on="IdTransacao")
df
# %%
df = df.groupby("IdCliente")["vlProduto"].sum().reset_index()
df = df.sort_values(by="vlProduto").head(n=1)
user = df["IdCliente"].loc[0]
# %%
print(f"O usuário com maior quantidade de pontos debitados é: {user}")
# %%
