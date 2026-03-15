import json

# Carrega o notebook
with open('/Users/marceliojeferson/Desktop/Dissertacao_Churn/dissertacao_churn.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Procura por seções 18-26 e examina o que vem depois
print("=== MAPEAMENTO DETALHADO: TÍTULO → CÓDIGO ===\n")

section_mapping = {}
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        content = ''.join(cell['source'])
        if '##' in content and any(str(num) in content for num in range(18, 27)):
            section = content.strip()
            print(f"\n📍 Célula {i}: {section}")
            
            # Procura próxima célula de código
            next_code_idx = None
            for j in range(i+1, min(i+3, len(nb['cells']))):
                if nb['cells'][j]['cell_type'] == 'code':
                    next_code_idx = j
                    break
            
            if next_code_idx is not None:
                code = ''.join(nb['cells'][next_code_idx]['source'])
                # Procura marcadores de modelo
                model_info = None
                if 'best_xgb' in code:
                    model_info = "🔴 XGBoost (best_xgb)"
                elif 'best_rf' in code:
                    model_info = "🟢 Random Forest (best_rf)"
                elif 'best_lgb' in code:
                    model_info = "🟡 LightGBM (best_lgb)"
                elif 'best_cat' in code:
                    model_info = "🟣 CatBoost (best_cat)"
                elif 'best_lr' in code:
                    model_info = "🔵 Logistic Regression (best_lr)"
                elif 'LIME' in code or 'lime' in code:
                    model_info = "🟠 LIME (Local Explainability)"
                else:
                    # Busca primeira linha significativa
                    for line in code.split('\n')[:20]:
                        if line.strip() and not line.strip().startswith('#'):
                            model_info = f"? {line.strip()[:60]}"
                            break
                
                print(f"   └→ Código associado (célula {next_code_idx}): {model_info}")
            else:
                print(f"   └→ Nenhuma célula de código próxima")

