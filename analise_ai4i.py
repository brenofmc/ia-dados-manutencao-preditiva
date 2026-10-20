import pandas as pd

# Carrega a base AI4I 2020
df = pd.read_csv("ai4i2020.csv")

sensores = ["Air temperature [K]", "Process temperature [K]",
            "Rotational speed [rpm]", "Torque [Nm]", "Tool wear [min]"]

# 1. Verificacao de integridade
print("Nulos por coluna:\n", df.isnull().sum())
print("\nLinhas duplicadas:", df.duplicated().sum())

# 2. Resumo estatistico
print("\nEstatistica dos sensores:\n", df[sensores].describe())

# 3. Deteccao de outliers por IQR (sem remover)
for c in sensores:
    q1, q3 = df[c].quantile(0.25), df[c].quantile(0.75)
    iqr = q3 - q1
    lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    n = ((df[c] < lo) | (df[c] > hi)).sum()
    print(f"{c}: {n} outliers em [{lo:.1f}, {hi:.1f}]")
