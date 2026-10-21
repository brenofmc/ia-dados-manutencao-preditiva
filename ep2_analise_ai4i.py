"""
EP II - Analise, Tratamento e Visualizacao de Dados com Python
Dataset: AI4I 2020 Predictive Maintenance (UCI)
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. CARREGAMENTO
df = pd.read_csv("ai4i2020.csv")
print("Dimensoes:", df.shape)

# 2. PADRONIZACAO DE CABECALHOS (snake_case)
df = df.rename(columns={
    "Air temperature [K]": "air_temp_k",
    "Process temperature [K]": "process_temp_k",
    "Rotational speed [rpm]": "rot_speed_rpm",
    "Torque [Nm]": "torque_nm",
    "Tool wear [min]": "tool_wear_min",
})

# 3. CONVERSAO DE TIPOS (Type como categoria; alvo segue numerico 0/1)
df["Type"] = df["Type"].astype("category")

# 4. VERIFICACAO DE INTEGRIDADE (base ja integra: 0 nulos, 0 duplicatas)
print("Nulos:", int(df.isnull().sum().sum()))
print("Duplicatas:", int(df.duplicated().sum()))
df = df.drop_duplicates()   # preventivo

# 5. VARIAVEIS DERIVADAS (operacoes vetoriais)
df["delta_temp"] = df["process_temp_k"] - df["air_temp_k"]
df["potencia_w"] = df["torque_nm"] * df["rot_speed_rpm"] * (2*np.pi/60)

# 6. ANALISE EXPLORATORIA (groupby)
alvo = "Machine failure"
sensores = ["air_temp_k","process_temp_k","rot_speed_rpm","torque_nm","tool_wear_min"]
print("\nMedias por grupo de falha:\n", df.groupby(alvo)[sensores].mean().round(2))
print("\nTaxa de falha por tipo (%):\n", (df.groupby("Type")[alvo].mean()*100).round(2))

# 7. VISUALIZACOES -> pasta graficos/
ok, fail = df[df[alvo]==0], df[df[alvo]==1]
C_OK, C_FAIL = "#4C72B0", "#C44E52"

# G1 boxplots
fig, ax = plt.subplots(1, 2, figsize=(10,5))
for a, col, lab in zip(ax, ["torque_nm","tool_wear_min"], ["Torque [N·m]","Desgaste [min]"]):
    bp = a.boxplot([ok[col], fail[col]], tick_labels=["Sem falha","Com falha"], patch_artist=True)
    for p, c in zip(bp['boxes'], [C_OK, C_FAIL]): p.set_facecolor(c); p.set_alpha(0.6)
    a.set_ylabel(lab); a.grid(axis='y', alpha=0.3)
fig.suptitle("Distribuicao por grupo de falha", fontweight='bold'); fig.tight_layout()
fig.savefig("graficos/g1_boxplot.png", dpi=150, bbox_inches='tight')

# G2 dispersao
fig, ax = plt.subplots(figsize=(9,6))
ax.scatter(ok["rot_speed_rpm"], ok["torque_nm"], s=8, alpha=0.25, color=C_OK, label="Sem falha")
ax.scatter(fail["rot_speed_rpm"], fail["torque_nm"], s=22, alpha=0.9, color=C_FAIL,
           label="Com falha", edgecolor='k', linewidth=0.3)
ax.set_xlabel("Velocidade de rotacao [rpm]"); ax.set_ylabel("Torque [N·m]")
ax.legend(); ax.grid(alpha=0.3); fig.tight_layout()
fig.savefig("graficos/g2_dispersao.png", dpi=150, bbox_inches='tight')

# G3 histograma
fig, ax = plt.subplots(figsize=(9,6))
ax.hist(ok["torque_nm"], bins=40, density=True, alpha=0.6, color=C_OK, label="Sem falha")
ax.hist(fail["torque_nm"], bins=40, density=True, alpha=0.6, color=C_FAIL, label="Com falha")
ax.set_xlabel("Torque [N·m]"); ax.set_ylabel("Densidade"); ax.legend(); fig.tight_layout()
fig.savefig("graficos/g3_histograma.png", dpi=150, bbox_inches='tight')

# G4 barras
taxa = (df.groupby("Type")[alvo].mean()*100).reindex(["L","M","H"])
fig, ax = plt.subplots(figsize=(8,5.5))
b = ax.bar(["L (baixa)","M (media)","H (alta)"], taxa.values, color=["#C44E52","#DD8452","#4C72B0"])
for bar, v in zip(b, taxa.values): ax.text(bar.get_x()+bar.get_width()/2, v+0.05, f"{v:.2f}%", ha='center', fontweight='bold')
ax.set_ylabel("Taxa de falha [%]"); ax.set_xlabel("Tipo de qualidade"); fig.tight_layout()
fig.savefig("graficos/g4_barras.png", dpi=150, bbox_inches='tight')

print("\nGraficos salvos em graficos/")
