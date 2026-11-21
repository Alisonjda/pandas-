# APPLY


# %% 

import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head(5)

# %%

idcliente = "000dc0f6-e4f2-4a42-b8cd-b586ed1c709a"

# %%
idcliente.split("-")[-1]

# %%
def get_last_id(x):
    return x.split("-")[-1]

# %%
novo_id = []

for i in df["idCliente"]:
    novo = get_last_id(i)
    novo_id.append(novo)

novo_id

# %%

df["novo_id"] = novo_id
df
# %%

df["idCliente"].apply(get_last_id)