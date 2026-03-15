#!/usr/bin/env python3
import json

# Load notebook
with open('dissertacao_churn.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Fix duplicates and missing sections
fixes = {
    "## 15 – Importância global com SHAP": "## 18 – SHAP para XGBoost",
    "## 16 – SHAP global (Random Forest)": "## 19 – SHAP para Random Forest",
    "## 17 – SHAP global (LightGBM)": "## 20 – SHAP para LightGBM",
}

count = 0
for cell in nb.get('cells', []):
    if cell.get('cell_type') == 'markdown':
        source = cell.get('source', [])
        for i, line in enumerate(source):
            for old, new in fixes.items():
                if old in line:
                    cell['source'][i] = line.replace(old, new)
                    print(f"✅ Corrigido: {old} → {new}")
                    count += 1

# Save
with open('dissertacao_churn.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print(f"\n✅ {count} seções corrigidas! Notebook atualizado com seções 18 e 19 restauradas!")
