# Rodomax HUB

Sistema de integração e saneamento de dados desenvolvido para o projeto UNIVEL x RODOMAX.

## Objetivo

Centralizar dados de demandas de frete provenientes de diferentes fontes (CSV, JSON e XLSX), realizar limpeza, normalização e validação, classificar anomalias com IA e armazenar os dados tratados em um banco PostgreSQL. Uma API e um painel web permitem consultar e cadastrar demandas.

## Tecnologias

- Python, Pandas, scikit-learn (IsolationForest)
- PostgreSQL, SQLAlchemy, Psycopg
- Flask (API)
- HTML, CSS e JavaScript (frontend)

## Estrutura

- `data/raw`: arquivos de dados brutos (CSV, JSON, XLSX)
- `data/processed`: saídas do pipeline (tratadas, normais, revisar, rejeitadas, duplicadas, logs)
- `src/config.py`: caminhos do projeto
- `src/banco.py`: conexão e inserção no PostgreSQL
- `src/limpeza.py`: remoção de incompletos e duplicados, validação
- `src/normalizacao.py`: normalização dos dados
- `src/ia_classificacao.py`: classificação de anomalias (NORMAL / REVISAR)
- `src/separacao.py`: separação das demandas em arquivos
- `src/pipeline.py`: orquestra o processamento
- `main.py`: executa o pipeline
- `api.py`: API Flask que também serve o frontend
- `frontend/`: painel web
- `bd_*.sql`: scripts do banco

## Como executar

1. Instalar dependências: `pip install -r requirements.txt`
2. Criar o banco, o schema e as tabelas com os scripts `bd_*.sql`
3. Processar os dados: `python main.py`
4. Iniciar a API e o painel: `python api.py` e abrir http://localhost:5000

## Endpoints da API

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/api/demandas` | Lista demandas (filtros opcionais `?fonte=CSV` e `?classificacao=REVISAR`) |
| POST | `/api/demandas` | Cadastra uma demanda (cliente, origem, destino, valor, fonte) |
| GET | `/api/resumo` | Totais por fonte e por classificação |
| GET | `/api/historico` | Histórico de importações |
| GET | `/api/saude` | Teste de conexão com o banco |
