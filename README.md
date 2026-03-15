# Dissertação Churn: Análise Preditiva de Rotatividade de Clientes

Este repositório contém o trabalho de dissertação/trabalho de conclusão de curso sobre **análise preditiva de churn (rotatividade de clientes)** em empresas de telecomunicações, utilizando técnicas avançadas de aprendizado de máquina.

## 🎯 Objetivo do Projeto

O estudo visa desenvolver um modelo preditivo robusto para identificar clientes com alta probabilidade de churn (cancelamento de serviços), permitindo intervenções proativas para retenção. O projeto abrange desde a exploração de dados até a implementação de modelos interpretáveis, com foco em:

- **Análise exploratória de dados (EDA)**: identificação de padrões e correlações em dados de clientes.
- **Pré-processamento**: tratamento de dados ausentes, codificação de variáveis categóricas e balanceamento de classes.
- **Modelagem**: comparação de algoritmos de classificação (Random Forest, XGBoost, LightGBM, CatBoost, Regressão Logística).
- **Avaliação**: métricas de desempenho (AUC, F1-Score, Precision, Recall) e validação cruzada estratificada.
- **Interpretabilidade**: uso de SHAP e LIME para explicar previsões do modelo.
- **Relatórios**: geração automática de relatórios em HTML/PDF com visualizações e insights.

O dataset utilizado é o **Telco Customer Churn** (IBM), contendo informações demográficas, de serviços e comportamentais de ~7.000 clientes.

---

## 🧩 Estrutura do Repositório

```
Dissertacao_Churn/
├── dissertacao_churn.ipynb      # Notebook principal com toda a análise
├── telco_churn.csv              # Dataset de clientes (fonte: IBM)
├── requirements.txt             # Dependências Python com versões
├── README.md                    # Este arquivo
├── .gitignore                   # Arquivos ignorados pelo Git
├── catboost_info/               # Logs e artefatos do CatBoost
└── *.py                         # Scripts auxiliares (se houver)
```

- **`dissertacao_churn.ipynb`**: Notebook Jupyter com seções organizadas (configuração, EDA, modelagem, avaliação, interpretabilidade).
- **`telco_churn.csv`**: Dados tabulares com 21 colunas (demografia, serviços, churn).
- **`requirements.txt`**: Lista de bibliotecas com versões mínimas recomendadas.
- **`catboost_info/`**: Diretório gerado automaticamente pelo CatBoost durante treinamento.

---

## 📚 Bibliotecas e Versões

O projeto utiliza as seguintes bibliotecas Python (versões testadas):

| Biblioteca | Versão Mínima | Função |
|------------|---------------|--------|
| **NumPy** | >= 1.21.0 | Operações numéricas com arrays |
| **Pandas** | >= 1.3.0 | Manipulação de dados tabulares |
| **Matplotlib** | >= 3.4.0 | Gráficos base |
| **Seaborn** | >= 0.11.0 | Visualizações estatísticas |
| **Scikit-learn** | >= 1.0.0 | Algoritmos ML e métricas |
| **XGBoost** | >= 1.5.0 | Gradient Boosting otimizado |
| **LightGBM** | >= 3.3.0 | Gradient Boosting eficiente |
| **CatBoost** | >= 1.0.0 | Gradient Boosting com categóricas |
| **Imbalanced-learn** | >= 0.8.0 | Técnicas de balanceamento (SMOTE) |
| **SHAP** | >= 0.40.0 | Interpretabilidade baseada em Shapley |
| **LIME** | >= 0.2.0 | Explicabilidade local |
| **Notebook/JupyterLab** | >= 6.4.0 / 3.0.0 | Ambiente de execução interativo |

> 🔍 **Como verificar versões instaladas**: Execute no terminal Python:
> ```python
> import numpy as np; print("NumPy:", np.__version__)
> # Repita para outras bibliotecas
> ```

---

## ✅ Instalação e Configuração

### Pré-requisitos
- **Python 3.8+** (recomendado 3.9 ou 3.10)
- **Git** (para clonar o repositório)
- **Jupyter Notebook** ou **JupyterLab** (instalado via pip)

### 1) Clonar o Repositório
```bash
git clone https://github.com/Marcelio2016/Dissertacao_churn.git
cd Dissertacao_Churn
```

### 2) Criar Ambiente Virtual (Recomendado)
```bash
python -m venv .venv
```

### 3) Ativar o Ambiente
- **macOS/Linux:**
  ```bash
  source .venv/bin/activate
  ```
- **Windows (Command Prompt):**
  ```cmd
  .venv\Scripts\activate
  ```
- **Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```

### 4) Instalar Dependências
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> ⚠️ **Nota**: Algumas bibliotecas (como XGBoost, LightGBM, CatBoost) podem requerer compiladores C++ no Windows. Se houver erros, consulte a documentação oficial de cada biblioteca.

### 5) Verificar Instalação
```bash
python -c "import numpy, pandas, sklearn, catboost; print('✅ Todas as bibliotecas instaladas!')"
```

---

## ▶️ Como Executar

### Opção 1: Notebook Completo (Recomendado)
```bash
jupyter notebook dissertacao_churn.ipynb
```
ou
```bash
jupyter lab dissertacao_churn.ipynb
```

Execute as células sequencialmente. O notebook está dividido em seções numeradas (1 a 29), cada uma com explicações detalhadas.

### Opção 2: Scripts Individuais (Se houver)
```bash
python nome_do_script.py
```

### Opção 3: Relatórios Gerados
- O notebook pode exportar relatórios em **HTML** (`dissertacao_churn.html`) e **PDF** (`dissertacao_churn.pdf`).
- Esses arquivos são ignorados pelo Git para manter o repositório leve.

---

<<<<<<< HEAD
## 📊 Resultados Esperados

Após execução completa, o projeto gera:
- **Modelos treinados**: salvos em `catboost_info/` ou similares.
- **Métricas de avaliação**: tabelas comparativas de performance (AUC > 0.85 esperado).
- **Visualizações**: gráficos de importância de features, matrizes de confusão, curvas ROC.
- **Explicações**: gráficos SHAP mostrando impacto de cada variável na previsão.

**Métricas principais**:
- **AUC-ROC**: ~0.85-0.90
- **F1-Score**: ~0.75-0.80
- **Precision/Recall**: balanceadas para classe minoritária (churn)

---

## 🛠️ Solução de Problemas

### Erro: "ModuleNotFoundError"
- Certifique-se de ativar o ambiente virtual: `source .venv/bin/activate`
- Reinstale dependências: `pip install -r requirements.txt`

### Erro: "No module named 'catboost'"
- Instale separadamente: `pip install catboost`
- No Windows, pode ser necessário Microsoft Visual C++ Build Tools.

### Notebook não abre
- Instale Jupyter: `pip install notebook jupyterlab`
- Execute: `jupyter notebook` ou `jupyter lab`

### Dados não carregam
- Verifique se `telco_churn.csv` está na pasta raiz.
- O notebook baixa dados alternativos do Google Sheets se necessário.

---

## 🚀 Próximos Passos e Melhorias

- **Deploy do modelo**: integrar com API (FastAPI/Flask) para previsões em produção.
- **Otimização**: hyperparameter tuning avançado, ensemble stacking.
- **Dados adicionais**: incorporar dados externos (econômicos, concorrência).
- **Monitoramento**: implementar tracking de performance em produção.

---

## 📄 Licença

Este projeto é para fins acadêmicos. Consulte orientador/orientadora para uso comercial.

---

## 📞 Contato

Para dúvidas sobre o projeto, abra uma **Issue** no GitHub ou entre em contato com o autor.
=======

>>>>>>> d7bb4e7635afda231de64cdbcef8575770295195
