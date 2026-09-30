# Qual o id do cliente no índice 4 no arquivo clientes.csv ?

# %%
import pandas as pd
df = pd.read_csv("../arquivos/clientes.csv", sep=";")
# %%
id_cliente = df.loc[4]["idCliente"]
# %%
print(f"O id do cliente é {id_cliente}")
# %%
