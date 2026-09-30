# Qual é o id de cliente que tem maior saldo de pontos? E o menor?

# %%
import pandas as pd
df = pd.read_csv("../arquivos/clientes.csv", sep=";")
# %%
df = df.sort_values(by="qtdePontos", ascending=False)
id_maior = df.iloc[0]["idCliente"]
id_menor = df.iloc[-1]["idCliente"]
# %%
print(f"O id com maior quantidade de pontos é: {id_maior}")
print(f"O id com menor quantidade de pontos é: {id_menor}")
# %%
