from src.banco import testar_conexao
from src.pipeline import processar_arquivos


def main():

    print("================================")
    print("       RODOMAX HUB")
    print("================================")

    testar_conexao()

    pasta = "data/raw"

    processar_arquivos(pasta)


if __name__ == "__main__":
    main()