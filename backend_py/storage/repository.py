from datetime import datetime


def registrar_log(mensagem):
    data = datetime.now()

    with open(
        "/home/ockham/Área de trabalho/Besteiras/Banco/data/banco.log", "a"
    ) as arquivo:
        arquivo.write(f"[{data}] - {mensagem}\n")
