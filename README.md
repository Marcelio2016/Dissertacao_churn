# Dissertação Churn

Este repositório contém o trabalho de dissertação/trabalho de conclusão sobre análise preditiva de churn (rotatividade de clientes) usando aprendizado de máquina.

O foco do projeto é: 
- carregar e preparar dados de clientes (CSV)
- treinar modelos (CatBoost, etc.)
- gerar relatórios e visualizações sobre a previsão de churn

---

## 🧩 Estrutura do repositório

- `dissertacao_churn.ipynb` — notebook principal com análise, modelagem e visualizações.
- `telco_churn.csv` — dataset usado para treinamento e avaliação (dados de clientes de telecom).
- `catboost_info/` — pastas geradas pelo CatBoost durante o treinamento (logs, modelos, etc.).
- `*.py` — scripts auxiliares (pré-processamento, diagnósticos, geração de relatórios).

---

## ✅ Requisitos (setup)

Recomenda-se usar um ambiente virtual Python para evitar conflitos de dependências.

### 1) Criar ambiente virtual

```bash
cd /Users/marceliojeferson/Desktop/Dissertacao_Churn
python -m venv .venv
```

### 2) Ativar o ambiente

- **macOS/Linux:**
  ```bash
  source .venv/bin/activate
  ```

- **Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```

### 3) Instalar dependências

Não existe um `requirements.txt` no repositório (ainda), então instale os pacotes principais manualmente:

```bash
pip install --upgrade pip
pip install pandas numpy scikit-learn catboost matplotlib seaborn notebook jupyterlab
```

> 🔎 Se você adicionar um `requirements.txt`, basta rodar:
> ```bash
> pip install -r requirements.txt
> ```

---

## ▶️ Como rodar

### 1) Executar o notebook (recomendado)

```bash
jupyter notebook dissertacao_churn.ipynb
```

ou (Jupyter Lab):

```bash
jupyter lab dissertacao_churn.ipynb
```

### 2) Executar scripts Python (opcional)

Alguns scripts podem ser praticados diretamente, por exemplo:

```bash
python analyze_content.py
python diagnose_sections.py
```

A maneira exata de usar cada script depende da lógica interna deles. Abra o script para ver o que ele espera como entrada.

---


