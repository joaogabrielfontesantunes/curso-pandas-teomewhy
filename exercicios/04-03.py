# Crie uma coluna que sinalize se a pessoa tem vínculo com alguma (qualquer uma) plataforma de rede social.

# %%
import pandas as pd
df = pd.read_csv("../arquivos/clientes.csv", sep=";")
# %%
df.head()
# %%
df["redeSocial"] = df[["flEmail", "flTwitch", "flYouTube", "flBlueSky", "flInstagram"]].sum(axis=1) > 0
df.head()
# %%
