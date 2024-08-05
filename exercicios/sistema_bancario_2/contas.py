# contas.py

contas = {}

def criar_conta(titular):
    if titular in contas:
        return False, "Já existe uma conta com esse titular."
    else:
        contas[titular] = 0
        return True, f"Conta criada para {titular}."

def depositar(titular, quantia):
    if titular in contas:
        if quantia > 0:
            contas[titular] += quantia
            return True, f"Depósito de R${quantia:.2f} realizado com sucesso."
        else:
            return False, "Quantia de depósito deve ser positiva."
    else:
        return False, "Conta não encontrada."

def retirar(titular, quantia):
    if titular in contas:
        if 0 < quantia <= contas[titular]:
            contas[titular] -= quantia
            return True, f"Saque de R${quantia:.2f} realizado com sucesso."
        else:
            return False, "Saque inválido. Verifique o saldo e a quantia solicitada."
    else:
        return False, "Conta não encontrada."

def verificar_saldo(titular):
    if titular in contas:
        return True, f"Saldo atual: R${contas[titular]:.2f}"
    else:
        return False, "Conta não encontrada."
