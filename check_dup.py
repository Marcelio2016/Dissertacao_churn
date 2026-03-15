import json

with open('/Users/marceliojeferson/Desktop/Dissertacao_Churn/dissertacao_churn.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Procurar pelos índices das células com código radar
print("=== VERIFICAÇÃO DE DUPLICAÇÃO - CÉLULAS 24-25 ===\n")

radar_cells = []
for i in range(len(nb['cells'])):
    if nb['cells'][i]['cell_type'] == 'code':
        code = ''.join(nb['cells'][i]['source'])
        if 'polar=True' in code:
            radar_cells.append(i)
            print(f"Célula {i}: Contém código RADAR")
            # Calcula tamanho
            lines_count = code.count('\n')
            print(f"  Linhas de código: {lines_count}")
            # Primeira função definida
            if 'def ' in code:
                for line in code.split('\n'):
                    if 'def ' in line:
                        print(f"  Função: {line.strip()[:60]}")
            print()

# Verifica se são idênticas
if len(radar_cells) >= 2:
    code1 = ''.join(nb['cells'][radar_cells[0]]['source'])
    code2 = ''.join(nb['cells'][radar_cells[1]]['source'])
    
    if code1 == code2:
        print("⚠️  AVISO: As duas células contêm código IDÊNTICO!")
        print("    Seção 25 parece ser uma duplicata de Seção 24")
    else:
        # Procura diferenças
        lines1 = code1.split('\n')
        lines2 = code2.split('\n')
        
        if len(lines1) == len(lines2):
            diffs = sum(1 for i, j in zip(lines1, lines2) if i != j)
            print(f"✅ Diferenças encontradas: {diffs} linhas diferentes")
        else:
            print(f"✅ Diferenças encontradas: Número de linhas diferente ({len(lines1)} vs {len(lines2)})")
