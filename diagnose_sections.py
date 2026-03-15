import json

# Carrega o notebook
with open('/Users/marceliojeferson/Desktop/Dissertacao_Churn/dissertacao_churn.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Procura por todas as seções a partir da seção 18
print("=== ANÁLISE DE SEÇÕES 18-26 ===\n")

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        content = ''.join(cell['source'])
        if '##' in content and any(str(num) in content for num in range(18, 27)):
            print(f"Célula {i}: {content.strip()}")
            # Próxima célula de código
            if i+1 < len(nb['cells']) and nb['cells'][i+1]['cell_type'] == 'code':
                code = ''.join(nb['cells'][i+1]['source'])
                # Extrai o primeiro significativo
                print("   Primeiras linhas do código:")
                for line in code.split('\n')[:15]:
                    if line.strip() and not line.strip().startswith('#'):
                        print(f"      {line[:100]}")
            print("-" * 120)
            print()
