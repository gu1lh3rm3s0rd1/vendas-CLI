Ferramenta em **Python 3.8+** para processar arquivos **CSV de vendas** e gerar relatórios completos, com suporte a múltiplos formatos de saída (texto, JSON e CSV).  
Ideal para análise rápida, integração com APIs ou exportação para planilhas.

---

## Funcionalidades

- Leitura de arquivos CSV de vendas.  
- Cálculo de:
  - Total de vendas por produto.  
  - Valor total de todas as vendas.  
  - Produto mais vendido.  
- Filtro opcional por intervalo de datas.  
- Saída nos formatos:
  - `text` — leitura humana (terminal).  
  - `json` — integração e automação.  
  - `csv` — exportação para Excel ou Power BI.  
- Logs informativos e tratamento robusto de erros.  
- Estrutura modular e testada (`pytest`).

---

## Estrutura do Projeto

```

vendas-cli/
│
├── src/
│   └── vendas_cli/
│       ├── **init**.py
│       ├── cli.py         ← Interface de linha de comando (CLI)
│       ├── parser.py      ← Leitura e normalização do CSV
│       ├── report.py      ← Lógica de cálculo dos relatórios
│       ├── output.py      ← Formatação da saída (text/json/csv)
│       └── main.py        ← Ponto de entrada manual (opcional)
│
├── tests/                 ← Testes unitários com pytest
│   ├── test_parser.py
│   ├── test_report.py
│   ├── test_output.py
│   └── test_output_csv.py
│
├── setup.py               ← Configuração de instalação (pip)
├── vendas.csv             ← Exemplo de arquivo de entrada
└── README.md

````

---

## Instalação

###  1. Criar ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate    # Windows
# ou
source venv/bin/activate # Linux / macOS
````

### 2. Instalar dependências e o pacote

```bash
pip install -e .
```

A flag `-e` instala o projeto em modo **editável**, permitindo modificar o código sem reinstalar.

---

##  Uso da CLI

###  Sintaxe básica

```bash
vendas-cli <arquivo_csv> [opções]
```

### 🔹 Exemplo simples

```bash
vendas-cli vendas.csv --format text
```

### 🔹 Exemplo com filtros de data e formato JSON

```bash
vendas-cli vendas.csv --format json --start 2025-01-01 --end 2025-03-31
```

### 🔹 Exemplo de exportação em CSV

```bash
vendas-cli vendas.csv --format csv
```

O relatório será exibido no terminal **e salvo automaticamente** como:

* `relatorio.json` (para `--format json`)
* `relatorio.csv` (para `--format csv`)

---

##  Testes

### Rodar todos os testes

```bash
pytest -v
```

### Rodar com relatório de cobertura

```bash
pytest --cov=src/vendas_cli --cov-report=term-missing -v
```
---

##  Requisitos

* Python **3.8+**
* Bibliotecas padrão (`csv`, `argparse`, `datetime`, `decimal`, `logging`, etc.)
* (Opcional) `pytest` e `pytest-cov` para rodar testes
