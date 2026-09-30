# Qual a quantidade média de redes sociais dos usuários? E a Variância? E o máximo?

# %%
import pandas as pd
df = pd.read_csv("../arquivos/clientes.csv", sep=";")
# %%
df["redeSocial"] = df[["flEmail", "flTwitch", "flYouTube", "flBlueSky", "flInstagram"]].sum(axis=1)
media = round(float(df["redeSocial"].mean()), 2)
variancia = round(df["redeSocial"].var(), 2)
max = df["redeSocial"].max()
# %%
print(
    f"A quantidade média de redes sociais dos usuários é: {media}\n"
    f"A variância de redes sociais dos usuários é: {variancia}\n"
    f"A quantidade máxima de redes sociais dos usuários é: {max}"
)
# %%
