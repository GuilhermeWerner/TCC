# Copyright (c) 2024 Guilherme Werner
# SPDX-License-Identifier: MIT

import pandas as pd
import matplotlib.pyplot as plt

data_file = "./trace/metrics.csv"
metrics_df_all = pd.read_csv(data_file)

metrics_df_all["protocol"] = metrics_df_all["test"].apply(
    lambda x: "TCP" if "TCP" in x else "UDP"
)

protocol_colors = {"TCP": "teal", "UDP": "orange"}
colors = metrics_df_all["protocol"].map(protocol_colors)

plt.figure(figsize=(6.4, 4.8))
plt.bar(metrics_df_all["test"], metrics_df_all["total_packets"], color=colors)
plt.title("Total de Pacotes por Teste")
plt.ylabel("Total de Pacotes")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("./trace/total_packets_comparison.png")
plt.close()

plt.figure(figsize=(6.4, 4.8))
plt.bar(metrics_df_all["test"], metrics_df_all["average_packet_size_kb"], color=colors)
plt.title("Tamanho Médio dos Pacotes por Teste")
plt.ylabel("Tamanho Médio dos Pacotes (kB)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("./trace/average_packet_size_comparison.png")
plt.close()

plt.figure(figsize=(6.4, 4.8))
plt.bar(metrics_df_all["test"], metrics_df_all["average_latency_ms"], color=colors)
plt.title("Latência Média por Teste")
plt.ylabel("Latência Média (ms)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("./trace/average_latency_comparison.png")
plt.close()

print("Gráficos gerados com sucesso.")
