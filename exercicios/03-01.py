# Quantos clientes tem vínculo com a Twitch?

# %%
import pandas as pd
df = pd.read_csv("../arquivos/clientes.csv", sep=";")
# %%
clientes_twitch = int(df["flTwitch"].sum())
# %%
print(f"A quantidade de clientes que têm vínculo com a Twitch é {clientes_twitch}")
# %%
