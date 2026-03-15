#!/usr/bin/env python3
import json

with open('dissertacao_churn.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Remove duplicate "## 20" cell
cells_to_keep = []
skip_next = False

for i, cell in enumerate(nb['cells']):
    if skip_next:
        skip_next = False
        continue
    
    if cell.get('cell_type') == 'markdown':
        source = cell.get('source', [])
        text = ''.join(source) if isinstance(source, list) else source
        
        # If this is "## 20 – SHAP para LightGBM" and we already have one, skip it
        if '## 20 – SHAP para LightGBM' in text:
            # Count how many times we've seen this
            count_20 = sum(1 for c in cells_to_keep 
                          if c.get('cell_type') == 'markdown' and 
                          '## 20' in ''.join(c.get('source', [])))
            if count_20 > 0:  # We already have section 20, so skip this duplicate
                print(f"⏭️  Pulando célula duplicada: ## 20 – SHAP para LightGBM (cells_idx {i})")
                continue
    
    cells_to_keep.append(cell)

nb['cells'] = cells_to_keep

with open('dissertacao_churn.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print(f"✅ Duplicata removida! Notebook tem agora {len(nb['cells'])} células")
