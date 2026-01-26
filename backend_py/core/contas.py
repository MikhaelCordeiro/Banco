import random

from backend_py.storage.database import supabase
from backend_py.utils import security


def validar_cpf(cpf: str):
    uniqueValue = supabase.table("contas").select("*").eq("cpf", cpf).execute()
    if uniqueValue.data == []:
        return True
    else:
        return False


def gerar_numero_conta():
    while True:
        numero = random.randint(100000, 999999)

        response = supabase.table("contas").select("*").eq("numero", numero).execute()

        if not response.data:
            return numero


def criar_conta(cpf: str, senha: str):
    if not validar_cpf(cpf):
        return "CPF já esta em uso"

    if not security.verificar_forca(senha):
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
        return supabase.table("contas").insert(nova_conta).execute()
    except Exception as e:
        return f"Erro ao criar conta: {e}"
