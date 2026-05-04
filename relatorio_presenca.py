import pandas as pd
from datetime import date

# Leitura dos dados
df = pd.read_csv("dados/presenca.csv")

# Totais por aluno
total_dias = df.groupby("Nome")["Status"].count()
presencas = df[df["Status"] == "Presente"].groupby("Nome")["Status"].count()

# Relatório consolidado
relatorio = pd.DataFrame({
    "Total de Dias": total_dias,
    "Presenças": presencas,
}).fillna(0).astype(int)

relatorio["Faltas"] = relatorio["Total de Dias"] - relatorio["Presenças"]
relatorio["Frequência (%)"] = (relatorio["Presenças"] / relatorio["Total de Dias"] * 100).round(1)
relatorio["Risco de Evasão"] = relatorio["Frequência (%)"].apply(
    lambda x: "🔴 Alto" if x < 60 else ("🟡 Médio" if x < 75 else "🟢 Baixo")
)

# Exibe no terminal
print("\n===== RELATÓRIO DE PRESENÇA =====")
print(f"Gerado em: {date.today()}\n")
print(relatorio.to_string())
print("\n=================================\n")

# Exporta para Excel
relatorio.to_excel("relatorio_saida.xlsx", index=True)
print("Arquivo 'relatorio_saida.xlsx' gerado com sucesso!")