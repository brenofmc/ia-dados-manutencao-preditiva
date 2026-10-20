# ia-dados-manutencao-preditiva

# Integração e Análise de Dados em Sistemas de Engenharia

Projeto desenvolvido na disciplina **Inteligência Artificial e Programação para Engenharia**. Primeira de uma série de experiências práticas que percorrem o ciclo completo de análise de dados aplicada à engenharia: da coleta de dados de sensores até um agente de diagnóstico de manutenção e um dashboard interativo.

## Objetivo
Selecionar, caracterizar, classificar e tratar uma base de medições de sensores voltada à **manutenção preditiva** (Indústria 4.0), documentando cada decisão metodológica de forma reprodutível e auditável.

## Base de dados
- **AI4I 2020 Predictive Maintenance Dataset** — UCI Machine Learning Repository
- 10.000 registros, 14 variáveis, formato CSV (~510 KB)
- Licença Creative Commons CC BY 4.0
- Fonte: https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset

## Variáveis de sensor
| Variável | Grandeza | Unidade |
|---|---|---|
| Air temperature | Térmica | K |
| Process temperature | Térmica | K |
| Rotational speed | Mecânica (rotação) | rpm |
| Torque | Mecânica (torque) | N·m |
| Tool wear | Desgaste (tempo) | min |

## Resumo estatístico (10.000 registros)
| Variável | Mín | Máx | Média | Desvio |
|---|---|---|---|---|
| Air temperature [K] | 295,30 | 304,50 | 300,00 | 2,00 |
| Process temperature [K] | 305,70 | 313,80 | 310,01 | 1,48 |
| Rotational speed [rpm] | 1168 | 2886 | 1538,78 | 179,28 |
| Torque [Nm] | 3,80 | 76,60 | 39,99 | 9,97 |
| Tool wear [min] | 0 | 253 | 107,95 | 63,65 |

## Tratamento e limpeza
- **Nulos:** verificados com `df.isnull().sum()` — nenhum nulo e nenhuma duplicata nos 10.000 registros.
- **Outliers:** avaliados por IQR (1,5×). Rotação (418 pontos) e torque (69 pontos) além dos limites foram **mantidos**, por serem fisicamente coerentes e por representarem as condições extremas em que as falhas ocorrem — descartá-los enviesaria o modelo preditivo.
- **Ordenação:** crescente pela coluna `UDI` (índice sequencial 1–10.000), preservando a ordem original de aquisição.

## Tecnologias
Python 3 · Pandas

## Status do projeto
- [x] EP I — Coleta, classificação e documentação
- [ ] EP II — Análise e tratamento em Python
- [ ] EP III — Agente inteligente de diagnóstico de manutenção
- [ ] EP IV — Dashboard interativo

---
Base de dados: Matzka, S. (2020). *AI4I 2020 Predictive Maintenance Dataset*. UCI Machine Learning Repository. Licença CC BY 4.0.
