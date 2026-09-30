# Quantas colunas do tipo object há no arquivo produtos.csv ?

# %%
import pandas as pd
df = pd.read_csv("../arquivos/produtos.csv", sep=";")
# %%
qnt_obj = df.select_dtypes(include='object').shape[1]
# %%
print(f"A quantidade de colunas \"Object\" é {qnt_obj}")
# %%