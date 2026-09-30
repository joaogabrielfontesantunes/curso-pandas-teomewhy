# Quantas colunas do tipo int há no arquivo transacoes.csv ?

# %%
import pandas as pd
df = pd.read_csv("../arquivos/transacoes.csv", sep=";")
# %%
qnt_int = df.select_dtypes(include='int').shape[1]
# %%
print(f"A quantidade de colunas \"Int\" é {qnt_int}")
# %%
