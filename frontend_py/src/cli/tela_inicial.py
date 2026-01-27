import getpass

from backend_py.core import contas


def tela_inicial():
    print("Seja Bem-Vindo ao PyBank!")

    print("1.Criar Conta PyBank\n2.Já Tenho Conta PyBank")


def escolha():
    escolher = input("Digite (1 ou 2): ")
    if escolher == "1":
        cadastro1()
    elif escolher == "2":
        logi()
    else:
        print("Error, tente novamente")
        return False


# Colocar um try/except no cadastro1()


def cadastro1():
    cpf = input("Digite Seu Cpf: ")
    senha = getpass.getpass("Digite Sua Senha(Somente Numerais): ")
    print(contas.criar_conta(cpf, senha))
    return True


def logi():
    login_cpf = input("Digite Seu Cpf: ")
    login_senha = getpass.getpass("Digite Sua Senha: ")
    print("Login Concluido!")
    return True


def main():
    while True:
        tela_inicial()
        resultado = escolha()
        if resultado == True:
            break


if __name__ == "__main__":
    main()
