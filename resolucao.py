import copy
menu_saque = "\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[l] Listar contas\n[n] Nova conta\n[q] Sair\n=> "
menu_init = "\n[n] Nova conta\n[l] Logar\n[q] Sair\n=> "
accont_On = False
cpf = None
accont = {'numero': 0 ,'agencia': '0001','saldo': 0,'saque_max': 500,'extrato':'', 'n_saques' : 0}
user_base = {123: {'info': ['rafael', '01022003', 123, 'lalalala'],"conts": [{'numero': 0 ,'agencia': '0001','saldo': 1000,'saque_max': 500,'extrato':'', 'n_saques' : 0}]}}

def user_sing_in(user_cpf:int, users = user_base):
    if user_cpf in users:
        print(f"{'='*42}\nlogado")
        return True
    else:
        print('Cpf invalido!')
        return False

def user_new( nome:str, nascimento:str, user_cpf:int, endereco:str, users = user_base, cpf = cpf):
    if user_cpf in users:
        print(f"{'='*42}\n")
        print('cpf já cadastrado')
        return False
        
    user_new = {'info': [nome, nascimento, user_cpf, endereco], 'conts': [accont]}
    users[user_cpf] = user_new
    cpf = user_cpf
    print(f"{'='*42}\n")
    print("usuario criado!")
    return True

def accont_list(user_cpf:int, users = user_base):
    user = users.get(user_cpf)
    for conts in user['conts']:
        print(f'numero: {conts['numero']} | saldo: {conts['saldo']} | saques_restantes:{conts['n_saques']}')

def accont_new(user_cpf, users = user_base):
    agencia = '0001'
    numero = len(users.get(user_cpf)['conts'])
    new_accont = copy.deepcopy(accont)
    
    new_accont['numero'] = numero
    new_accont['agencia'] = agencia
    users.get(user_cpf)['conts'].append(new_accont)
    print('cadastrado')
          
def accont_saque(user_cpf, users = user_base):
    number_accont = int(input('numero de conta: '))
    saque = int(input('valor do saque: '))
    
    user_accont = users.get(user_cpf)['conts'][number_accont]
    user_saques = user_accont['n_saques']
    user_saldo = user_accont['saldo']
    max_saque = 3
    limite_saque = 500
    
    excedeu_saldo = saque > user_saldo
    excedeu_limite = saque > limite_saque
    excedeu_saques = user_saques >= max_saque
    
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif saque > 0:
        user_accont['saldo'] -= saque
        user_accont['extrato'] += f"Saque: R$ {saque:.2f}\n"
        user_accont['n_saques'] += 1
    
def accont_deposito(user_cpf, users = user_base):
    user_acconts = users.get(user_cpf)['conts']

    number_accont = int(input('numeor da conta: '))
    if number_accont <= len(user_acconts)-1: 
        deposito = float(input('valor do deposito: '))   
        if deposito > 0:
            user_accont = user_acconts[number_accont] 
            user_accont['saldo'] += deposito
            user_accont['extrato'] += f"Depósito: R$ {deposito:.2f}\n"
            print('deposito realizado')
        else:
            return("Operação falhou! O valor informado é inválido.")
        
def accont_extrato(user_cpf, users = user_base):
    user_acconts = users.get(user_cpf)['conts']
    number_accont = int(input('numeor da conta: '))

    if number_accont <= len(user_acconts)-1: 
        extrato = user_acconts[number_accont]['extrato']
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f'saldo: {user_acconts[number_accont]['saldo']}')
        print('='*42)
    else:
        print('numero invalido\n')

def accont_operation(cpf):
    while True:
        option = input(menu_saque)
        if option == "d":
            accont_deposito( user_cpf=cpf)

        elif option == "s":
            accont_saque(user_cpf=cpf)

        elif option == "e":
            accont_extrato(user_cpf=cpf)

        elif option == 'l':
            accont_list(cpf)

        elif option == 'n':
            accont_new(user_cpf=cpf)
        
        elif option == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            


while True:
    option = input(menu_init)
    if option == 'n':
        nome = input("nome: ")
        cpf_new = int(input("cpf: "))
        nascimento = input("nascimento: ")
        endereco = input("endereço: ")
        if user_new(nome=nome,nascimento=nascimento,user_cpf=cpf_new,endereco=endereco):
            cpf = cpf_new
            accont_On = True
            
    elif option == 'l':
        cpf_login = int(input('digite seu cpf:'))
        if user_sing_in(user_cpf=cpf_login):
            cpf = cpf_login
            accont_On = True
            
    elif option == 'q':
        break

    if accont_On:
        accont_operation(cpf)
    