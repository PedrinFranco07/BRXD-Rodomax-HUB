from sqlalchemy import create_engine, text


# ==========================================
# CONFIGURAÇÃO DO POSTGRESQL
# ==========================================

USUARIO = "postgres"
SENHA = "jarschel12"
HOST = "localhost"
PORTA = "5432"
BANCO = "rodomax_hub"

DATABASE_URL = (
    f"postgresql+psycopg://"
    f"{USUARIO}:{SENHA}@{HOST}:{PORTA}/{BANCO}"
)

engine = create_engine(DATABASE_URL)


# ==========================================
# TESTAR CONEXÃO
# ==========================================

def testar_conexao():
    try:
        with engine.connect() as conexao:
            print("Conexão com PostgreSQL realizada com sucesso!")

    except Exception as erro:
        print("Erro ao conectar com PostgreSQL:")
        print(erro)


# ==========================================
# INSERIR DEMANDAS
# ==========================================

def inserir_dados(df):

    print("\n========== POSTGRESQL ==========")

    registros_inseridos = 0
    registros_ignorados = 0

    try:

        with engine.begin() as conexao:

            for _, registro in df.iterrows():

                resultado = conexao.execute(
                    text("""
                        INSERT INTO rodomax.demandas (
                            cliente,
                            email,
                            telefone,
                            origem,
                            destino,
                            valor_frete,
                            fonte
                        )
                        VALUES (
                            :cliente,
                            :email,
                            :telefone,
                            :origem,
                            :destino,
                            :valor_frete,
                            :fonte
                        )
                        ON CONFLICT DO NOTHING
                    """),
                    {
                        "cliente": registro["cliente"],
                        "email": registro["email"],
                        "telefone": registro["telefone"],
                        "origem": registro["origem"],
                        "destino": registro["destino"],
                        "valor_frete": registro["valor_frete"],
                        "fonte": registro["fonte"]
                    }
                )

                if resultado.rowcount > 0:
                    registros_inseridos += 1
                else:
                    registros_ignorados += 1

        print(
            f"Novos registros inseridos: {registros_inseridos}"
        )

        print(
            f"Registros já existentes ignorados: {registros_ignorados}"
        )

        return registros_inseridos, registros_ignorados

    except Exception as erro:

        print("Erro ao inserir dados no PostgreSQL:")
        print(erro)

        return 0, 0


# ==========================================
# REGISTRAR HISTÓRICO DA IMPORTAÇÃO
# ==========================================

def registrar_importacao(
    arquivos_processados,
    registros_recebidos,
    registros_incompletos,
    duplicados_removidos,
    registros_finais,
    registros_inseridos,
    registros_ignorados
):

    try:

        with engine.begin() as conexao:

            conexao.execute(
                text("""
                    INSERT INTO rodomax.importacoes (
                        arquivos_processados,
                        registros_recebidos,
                        registros_incompletos,
                        duplicados_removidos,
                        registros_finais,
                        registros_inseridos,
                        registros_ignorados
                    )
                    VALUES (
                        :arquivos_processados,
                        :registros_recebidos,
                        :registros_incompletos,
                        :duplicados_removidos,
                        :registros_finais,
                        :registros_inseridos,
                        :registros_ignorados
                    )
                """),
                {
                    "arquivos_processados": arquivos_processados,
                    "registros_recebidos": registros_recebidos,
                    "registros_incompletos": registros_incompletos,
                    "duplicados_removidos": duplicados_removidos,
                    "registros_finais": registros_finais,
                    "registros_inseridos": registros_inseridos,
                    "registros_ignorados": registros_ignorados
                }
            )

        print(
            "Histórico da importação registrado com sucesso!"
        )

    except Exception as erro:

        print("Erro ao registrar histórico da importação:")
        print(erro)