import pandas as pd
import re


def remover_registros_incompletos(df):

    print("\n========== LIMPEZA DOS DADOS ==========")

    registros_antes = len(df)

    colunas_obrigatorias = [
        "cliente",
        "origem",
        "destino"
    ]

    df = df.dropna(subset=colunas_obrigatorias)

    registros_depois = len(df)

    removidos = registros_antes - registros_depois

    print(f"Registros antes da limpeza: {registros_antes}")
    print(f"Registros incompletos removidos: {removidos}")
    print(f"Registros restantes: {registros_depois}")

    return df, removidos


def remover_duplicados(df):

    print("\n========== REMOÇÃO DE DUPLICADOS ==========")

    registros_antes = len(df)

    df = df.drop_duplicates()

    registros_depois = len(df)

    duplicados_removidos = registros_antes - registros_depois

    print(f"Registros antes: {registros_antes}")
    print(f"Duplicados removidos: {duplicados_removidos}")
    print(f"Registros restantes: {registros_depois}")

    return df, duplicados_removidos


def validar_email(email):

    if email == "":
        return True

    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return bool(re.match(padrao, email))


def validar_telefone(telefone):

    if telefone == "":
        return True

    return len(telefone) in [10, 11]


def validar_valor(valor):

    if pd.isna(valor):
        return False

    return valor > 0


def validar_dados(df):

    print("\n========== VALIDAÇÃO DOS DADOS ==========")

    emails_invalidos = 0
    telefones_invalidos = 0
    valores_invalidos = 0

    for email in df["email"]:
        if not validar_email(email):
            emails_invalidos += 1

    for telefone in df["telefone"]:
        if not validar_telefone(telefone):
            telefones_invalidos += 1

    for valor in df["valor_frete"]:
        if not validar_valor(valor):
            valores_invalidos += 1

    print(f"E-mails inválidos: {emails_invalidos}")
    print(f"Telefones inválidos: {telefones_invalidos}")
    print(f"Valores de frete inválidos: {valores_invalidos}")

    return df