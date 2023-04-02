faturamento_diario = [31490.7866, 37277.9400, 37708.4303, 0.0000, 0.0000, 17934.2269, 0.0000, 6965.1262, 24390.9374, 14279.6481, 0.0000, 0.0000, 39807.6622, 27261.6304, 39775.6434, 29797.6232, 17216.5017, 0.0000, 0.0000, 12974.2000, 28490.9861, 8748.0937, 8889.0023, 17767.5583, 0.0000, 0.0000, 3071.3283, 48275.2994, 10299.6761, 39874.1073]
menor_faturamento = min(faturamento_diario)
print(f"Menor faturamento diário: {menor_faturamento:.2f}")

maior_faturamento = max(faturamento_diario)
print(f"Maior faturamento diário: {maior_faturamento:.2f}")

media_mensal = sum(faturamento_diario) / len(faturamento_diario)

dias_acima_da_media = sum(1 for faturamento in faturamento_diario if faturamento > media_mensal)
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
