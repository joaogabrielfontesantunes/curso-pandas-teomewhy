# Quais são os usuários que mais fizeram transações? Considere os 10 primeiros.

# %%
import pandas as pd
df = pd.read_csv("../arquivos/transacoes.csv", sep=";")
# %%
resultado = (df.groupby("IdCliente").size()
             .reset_index())
resultado.columns = (["IdCliente", "QtdeTransacao"])
# %%
resultado = resultado.sort_values(by="QtdeTransacao", ascending=False)
resultado = resultado.head(n=10)["IdCliente"].tolist()
# %%
print("Os 10 usuários com mais transações são:")
for posicao, nome in enumerate(resultado, start=1):
    print(f"{posicao}. {nome}")
# %%
