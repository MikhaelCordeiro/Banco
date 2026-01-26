import hashlib
import re
import secrets


def verificar_forca(senha):
    return len(senha) >= 8 and re.search(r"\d", senha) and re.search(r"[A-Z]", senha)


def salt():
    return secrets.token_hex(16)


def hash_senha(senha, salt):
    return hashlib.pbkdf2_hmac(
        "sha256", senha.encode("utf-8"), salt.encode("utf-8"), 600000
    ).hex()


def validar_senha(senha_digitada, salt_salvo, hash_salvo):
    return secrets.compare_digest(hash_salvo, hash_senha(senha_digitada, salt_salvo))
