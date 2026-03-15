import json

# Carrega e altera títulos corretamente
with open('/Users/marceliojeferson/Desktop/Dissertacao_Churn/dissertacao_churn.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Correções finais CORRETAS
corrections = {
    "## 21 – SHAP para LightGBM (Top-10)": "## 21 – Top 10 Variáveis Mais Importantes (SHAP)",
    "## 22 – Explicabilidade Local com LIME (Exemplos de Clientes)": "## 22 – Explicabilidade Local com LIME (Inicialização)",
}

# Itera sobre as células
modified = 0
for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        source = cell['source']
        if isinstance(source, list):
            source_str = ''.join(source)
        else:
            source_str = source
        
        for old_title, new_title in corrections.items():
            if old_title in source_str:
                # Reconstrói o source com a correção
                if isinstance(cell['source'], list):
                    cell['source'] = [new_title if line.strip() == old_title else line for line in cell['source']]
                else:
                    cell['source'] = [new_title]
                print(f"✅ Seção corrigida: '{old_title}'")
                print(f"                 → '{new_title}'")
                modified += 1
                break

print(f"\n🔄 Total de títulos corrigidos: {modified}")

# Salva alterações
with open('/Users/marceliojeferson/Desktop/Dissertacao_Churn/dissertacao_churn.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("✅ Notebook atualizado com sucesso!")
