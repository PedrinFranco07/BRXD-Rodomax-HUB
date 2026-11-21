# Rodomax HUB

Sistema de integração e saneamento de dados desenvolvido para o projeto UNIVEL x RODOMAX.

## Objetivo

Centralizar dados provenientes de diferentes fontes, realizar limpeza, normalização e validação das informações e armazenar os dados tratados em um banco PostgreSQL.

## Tecnologias

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Psycopg
- VS Code

## Estrutura

- data/raw: arquivos de dados brutos
- data/processed: arquivos tratados
- src/banco.py: conexão com PostgreSQL
- src/limpeza.py: funções de limpeza
- src/normalizacao.py: normalização dos dados
- src/pipeline.py: processamento dos dados
- main.py: execução do sistema