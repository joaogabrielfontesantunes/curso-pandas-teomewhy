# Quantas linhas há no arquivo clientes.csv ?

# %%
import pandas as pd
df = pd.read_csv("../arquivos/clientes.csv", sep=";")
# %%
num_linhas = df.shape[0]
print(f"O número de linhas é {num_linhas}")
# %%
