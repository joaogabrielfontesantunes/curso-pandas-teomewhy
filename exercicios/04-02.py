# Aplique o log na coluna de saldo de pontos, criando uma coluna nova

# %%
import pandas as pd
import numpy as np
df = pd.read_csv("../arquivos/clientes.csv", sep = ";")
# %%
df["log"] = np.log(df["qtdePontos"]+1)
df.head()
# %%
