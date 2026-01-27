import random

from backend_py.storage.database import supabase
from backend_py.storage.repository import registrar_log
from backend_py.utils import security


def validar_cpf(cpf: str):
    uniqueValue = supabase.table("contas").select("*").eq("cpf", cpf).execute()
    return len(uniqueValue.data) == 0


def gerar_numero_conta():
    while True:
        numero = random.randint(100000, 999999)

        response = supabase.table("contas").select("*").eq("numero", numero).execute()

        if not response.data:
            return numero


def criar_conta(cpf: str, senha: str):
    if not validar_cpf(cpf):
        return "CPF já esta em uso"

    if not security.verificar_senha(senha):
        return "Senha não segue as Regras"

    meu_salt = security.salt()
    hash_final = security.hash_senha(senha, meu_salt)
    numero_final = gerar_numero_conta()

    nova_conta = {
        "numero": numero_final,
        "senha": hash_final,
        "salt": meu_salt,
        "cpf": cpf,
    }

    try:
        supabase.table("contas").insert(nova_conta).execute()
        registrar_log(f"Sucesso: Conta {numero_final} criada para CPF {cpf}")
        return f"Conta criada com sucesso! Seu número é {numero_final}"
    except Exception as e:
        return registrar_log(f"ERRO CRÍTICO: {e}")
