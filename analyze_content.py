import json

# Carrega e analisa detalhadamente
with open('/Users/marceliojeferson/Desktop/Dissertacao_Churn/dissertacao_churn.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Procura seções 21-25 e vê o REAL conteúdo do código
print("=== ANÁLISE DO CONTEÚDO REAL DO CÓDIGO (Seções 21-25) ===\n")

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        content = ''.join(cell['source'])
        if '## 21' in content or '## 22' in content or '## 23' in content or '## 24' in content or '## 25' in content:
            section = content.strip()
            print(f"\n🔹 {section}")
            print(f"   Célula markdown: {i}")
            
            # Procura próxima célula de código
            for j in range(i+1, min(i+3, len(nb['cells']))):
                if nb['cells'][j]['cell_type'] == 'code':
                    code = ''.join(nb['cells'][j]['source'])
                    # Procura conteúdo real
                    content_indicators = []
                    if 'pd.DataFrame' in code and 'Top' in code:
                        content_indicators.append("🟰 Top-10 SHAP (DataFrame ranking)")
                    if 'results_tunados' in code and 'barh' in code:
                        content_indicators.append("📊 Top-10 SHAP (Barras horizontais)")
                    if 'exp_churn' in code or 'explicacoes[' in code and 'as_pyplot' in code:
                        content_indicators.append("🟠 Visualização LIME (explicações)")
                    if 'df_plot' in code and 'polar=True' in code:
                        content_indicators.append("⛳ Radar (visualização comparativa)")
                    if 'df_melted' in code and 'barplot' in code:
                        content_indicators.append("📈 Barras Agrupadas (visualização comparativa)")
                    if 'scatter' in code and 'limiar_risco' in code:
                        content_indicators.append("🎯 Matriz Estratégica (Risco vs Valor)")
                    if 'lime_tabular' in code:
                        content_indicators.append("🔧 Setup LIME (inicialização)")
                    
                    if content_indicators:
                        print(f"   Célula código {j}: {', '.join(content_indicators)}")
                    else:
                        # Mostrar primeira linha significativa
                        first_line = None
                        for line in code.split('\n'):
                            if line.strip() and not line.strip().startswith('#'):
                                first_line = line.strip()[:60]
                                break
                        if first_line:
                            print(f"   Célula código {j}: ? {first_line}")
                    break
