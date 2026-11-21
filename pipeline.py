import pandas as pd
from pathlib import Path

from .logs import registrar_log
from src.banco import (
    inserir_dados,
    registrar_importacao
)
from src.limpeza import (
    remover_registros_incompletos,
    remover_duplicados,
    validar_dados
)
from src.normalizacao import (
    normalizar_textos,
    normalizar_email,
    normalizar_telefone
)


# ==========================================
# LEITURA DOS DADOS
# ==========================================

def ler_dados(caminho):

    extensao = caminho.suffix.lower()

    if extensao == ".csv":

        df = pd.read_csv(caminho)

    elif extensao == ".xlsx":

        df = pd.read_excel(caminho)

    elif extensao == ".json":

        df = pd.read_json(caminho)

    else:

        return None

    return df


# ==========================================
# BUSCA DOS ARQUIVOS
# ==========================================

def encontrar_arquivos(pasta):

    pasta = Path(pasta)

    arquivos = []

    for arquivo in pasta.iterdir():

        if arquivo.suffix.lower() in [".csv", ".xlsx", ".json"]:

            arquivos.append(arquivo)

    return arquivos


# ==========================================
# AUDITORIA INICIAL
# ==========================================

def auditoria_inicial(df):

    print("\n========== AUDITORIA INICIAL ==========")

    print(
        f"Total de registros: {len(df)}"
    )

    print("\nValores nulos por coluna:")

    print(
        df.isnull().sum()
    )

    print("\nRegistros duplicados:")

    print(
        df.duplicated().sum()
    )


# ==========================================
# SALVAR DADOS PROCESSADOS
# ==========================================

def salvar_dados_processados(df):

    caminho = Path(
        "data/processed/demandas_tratadas.csv"
    )

    # Garante que a pasta exista
    caminho.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        caminho,
        index=False,
        encoding="utf-8-sig"
    )

    print(
        "\n========== ARQUIVO PROCESSADO =========="
    )

    print(
        f"Arquivo salvo em: {caminho}"
    )


# ==========================================
# AUDITORIA FINAL
# ==========================================

def auditoria_final(
    registros_iniciais,
    registros_incompletos,
    duplicados,
    registros_finais
):

    print("\n========== AUDITORIA FINAL ==========")

    print(
        f"Registros recebidos:       "
        f"{registros_iniciais}"
    )

    print(
        f"Registros incompletos:     "
        f"{registros_incompletos}"
    )

    print(
        f"Duplicados removidos:      "
        f"{duplicados}"
    )

    print(
        f"Registros finais:          "
        f"{registros_finais}"
    )

    if registros_iniciais > 0:

        aproveitamento = (
            registros_finais /
            registros_iniciais
        ) * 100

        print(
            f"Taxa de aproveitamento:   "
            f"{aproveitamento:.2f}%"
        )


# ==========================================
# PROCESSAMENTO PRINCIPAL
# ==========================================

def processar_arquivos(pasta):

    print(
        "\n========== BUSCA DE ARQUIVOS =========="
    )

    # --------------------------------------
    # BUSCAR ARQUIVOS
    # --------------------------------------

    arquivos = encontrar_arquivos(pasta)

    if not arquivos:

        print("Nenhum arquivo encontrado.")

        return

    print(
        f"Arquivos encontrados: "
        f"{len(arquivos)}"
    )

    for arquivo in arquivos:

        print(
            f"- {arquivo.name}"
        )

    # ======================================
    # LEITURA DOS ARQUIVOS
    # ======================================

    print(
        "\n========== LEITURA DAS FONTES =========="
    )

    lista_dados = []

    for arquivo in arquivos:

        print(
            f"Lendo: {arquivo.name}"
        )

        df = ler_dados(arquivo)

        if df is not None:

            print(
                f"Registros encontrados: "
                f"{len(df)}"
            )

            # Identifica a origem do arquivo
            df["fonte"] = (
                arquivo
                .suffix
                .replace(".", "")
                .upper()
            )

            lista_dados.append(df)

    # --------------------------------------
    # VERIFICAR SE EXISTEM DADOS
    # --------------------------------------

    if not lista_dados:

        print(
            "Nenhum dado válido encontrado."
        )

        return

    # ======================================
    # UNIFICAÇÃO DOS LOTES
    # ======================================

    print(
        "\n========== UNIFICAÇÃO DOS LOTES =========="
    )

    df = pd.concat(
        lista_dados,
        ignore_index=True
    )

    # Guarda a quantidade original
    registros_iniciais = len(df)

    print(
        f"Total de registros recebidos: "
        f"{registros_iniciais}"
    )

    # ======================================
    # AUDITORIA INICIAL
    # ======================================

    auditoria_inicial(df)

    # ======================================
    # LIMPEZA
    # ======================================

    print(
        "\n========== LIMPEZA DOS DADOS =========="
    )

    df, registros_incompletos = (
        remover_registros_incompletos(df)
    )

    # ======================================
    # NORMALIZAÇÃO
    # ======================================

    print(
        "\n========== NORMALIZAÇÃO =========="
    )

    df = normalizar_textos(df)

    df = normalizar_email(df)

    df = normalizar_telefone(df)

    print(
        "Textos normalizados."
    )

    print(
        "E-mails normalizados."
    )

    print(
        "Telefones normalizados."
    )

    # ======================================
    # REMOÇÃO DE DUPLICADOS
    # ======================================

    print(
        "\n========== REMOÇÃO DE DUPLICADOS =========="
    )

    df, duplicados = remover_duplicados(df)

    # ======================================
    # VALIDAÇÃO
    # ======================================

    print(
        "\n========== VALIDAÇÃO DOS DADOS =========="
    )

    df = validar_dados(df)

    # ======================================
    # MOSTRAR DADOS TRATADOS
    # ======================================

    print(
        "\n========== DADOS TRATADOS =========="
    )

    print(
        df.to_string(index=False)
    )

    # ======================================
    # SALVAR ARQUIVO PROCESSADO
    # ======================================

    salvar_dados_processados(df)

    # ======================================
    # INSERIR NO POSTGRESQL
    # ======================================

    print(
        "\n========== POSTGRESQL =========="
    )

    registros_inseridos, registros_ignorados = (
        inserir_dados(df)
    )

    # ======================================
    # AUDITORIA FINAL
    # ======================================

    auditoria_final(
        registros_iniciais,
        registros_incompletos,
        duplicados,
        len(df)
    )

    # ======================================
    # REGISTRAR LOG
    # ======================================

    registrar_log(
        arquivos_processados=len(arquivos),
        registros_recebidos=registros_iniciais,
        registros_incompletos=registros_incompletos,
        duplicados_removidos=duplicados,
        registros_finais=len(df),
        registros_inseridos=registros_inseridos,
        registros_ignorados=registros_ignorados
    )

    registrar_importacao(
    arquivos_processados=len(arquivos),
    registros_recebidos=registros_iniciais,
    registros_incompletos=registros_incompletos,
    duplicados_removidos=duplicados,
    registros_finais=len(df),
    registros_inseridos=registros_inseridos,
    registros_ignorados=registros_ignorados
)