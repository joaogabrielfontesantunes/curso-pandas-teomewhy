# Quem teve mais transações de Streak?

# %%
import pandas as pd
df1 = pd.read_csv("../arquivos/transacao_produto.csv", sep=";")
df2 = pd.read_csv("../arquivos/transacoes.csv", sep=";")
# %%
filtro = df1["IdProduto"] == "12"
df1 = df1[filtro]
# %%
df = pd.merge(df1, df2, how="inner", on="IdTransacao")
# %%
df = df.groupby("IdCliente").size().reset_index(name="qtd").sort_values(by="qtd", ascending=False)
id_transacoes = df["IdCliente"].iloc[0]
# %%
print(f"{id_transacoes}")
# %%
