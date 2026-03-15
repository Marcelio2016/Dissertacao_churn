import json

# Carrega e altera títulos
with open('/Users/marceliojeferson/Desktop/Dissertacao_Churn/dissertacao_churn.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Mapear alterações corretas
corrections = {
    "## 18 – SHAP para XGBoost": "## 18 – SHAP para Random Forest",
    "## 19 – SHAP para Random Forest": "## 19 – SHAP para LightGBM",
    "## 20 – SHAP para LightGBM": "## 20 – SHAP para CatBoost",
    "## 21 – SHAP para CatBoost": "## 21 – SHAP para LightGBM (Top-10)",
    "## 22 – Regressão Logística (Explanações via SHAP)": "## 22 – Explicabilidade Local com LIME (Exemplos de Clientes)",
    "## 23 – Top 10 Variáveis Mais Importantes (SHAP)": "## 23 – Top 10 Variáveis Mais Importantes (SHAP)",
    "## 24 – Explicabilidade Local com LIME (Exemplos de Clientes)": "## 24 – Visualização Comparativa de Algoritmos (Radar e Barras)",
    "## 25 – Visualização Comparativa de Algoritmos (Radar e Barras)": "## 25 – Visualização Comparativa de Algoritmos (Radar e Barras)"
}

# Itera sobre as células
modified = 0
for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        source = cell['source']
        if isinstance(source, list):
            source = ''.join(source)
        
        for old_title, new_title in corrections.items():
            if old_title in source:
                # Reconstrói o source com a correção
                if isinstance(cell['source'], list):
                    cell['source'] = [new_title if line.strip() == old_title else line for line in cell['source']]
                else:
                    cell['source'] = [new_title]
                print(f"✅ Corrigido: '{old_title}' → '{new_title}'")
                modified += 1
                break

print(f"\n🔄 Total de títulos corrigidos: {modified}")

# Salva alterações
with open('/Users/marceliojeferson/Desktop/Dissertacao_Churn/dissertacao_churn.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("✅ Notebook atualizado com sucesso!")
