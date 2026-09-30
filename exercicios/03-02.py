# Quantos clientes tem um saldo de pontos maior que 1000?

# %%
import pandas as pd
df = pd.read_csv("../arquivos/clientes.csv", sep=";")
# %%
filtro = df["qtdePontos"] > 1000
qnt_filtro = df[filtro].shape[0]
# %%
print(f"A quantidade de clientes com saldo maior que 1000 é {qnt_filtro}")
# %%
