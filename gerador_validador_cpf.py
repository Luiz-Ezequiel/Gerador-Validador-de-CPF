import random, os

def cpf_sequencial(cpf):
    # Verifica se o cpf apresentado é sequencial: 111.111.111-11

    primeiro_digito = cpf[0]
    return cpf == primeiro_digito * len(cpf)

def gerar_nove_digitos():
    # Gera aleatóriamente os primeiros nove digitos do cpf

    nove_digitos = ''
    for _ in range(0,9):
        nove_digitos += str(random.randint(0,9))
    return nove_digitos

def calcula_digito(digitos_cpf):
    # Calcula o digito identificador do cpf a partir de 9 ou 10 digitos
    # Retorna o próximo digito (10 ou 11) como uma string

    if len(digitos_cpf) == 9:
        i = 10
    else:
        i = 11
    soma_digitos = 0
    for digitos in digitos_cpf:
        int_digitos = int(digitos)
        multiplicacao = int_digitos * i
        soma_digitos += multiplicacao
        i -= 1
    resto_divisao = (soma_digitos * 10) % 11 
    return "0" if resto_divisao > 9 else str(resto_divisao)

def gerar_cpf():
    # Gera um cpf aleatório e válido
    nove_digitos = gerar_nove_digitos()
    decimo_digito = calcula_digito(nove_digitos)
    decimo_primeiro_digito = calcula_digito(nove_digitos + decimo_digito)
    return nove_digitos + decimo_digito + decimo_primeiro_digito

def valida_cpf(cpf_usuario):
        cpf = cpf_usuario.replace(".", "").replace("-", "")
        nove_digitos = cpf[:9]
        if len(cpf) != 11 or not cpf.isdigit():
            return False
        if cpf_sequencial(nove_digitos):
            return False
        decimo_digito = calcula_digito(nove_digitos) 
        decimo_primeiro_digito = calcula_digito(nove_digitos + decimo_digito)
        return cpf == nove_digitos + decimo_digito + decimo_primeiro_digito

def formatar_cpf(cpf):
    # Formata o cpf, tirando os "." e "-"
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

while True:
    option = input("[v]alidação | [g]erar cpf | [s]air: ")
    if option == 's':
        os.system("cls")
        print("Obrigado por usar o programa!")
        break
    
    elif option == 'v':
        cpf_para_validar = input("Digite o cpf que deseja validar: ")
        if valida_cpf(cpf_para_validar):
            print("Seu cpf é valido\n")
        else:
            print("cpf inválido\n")
    
    elif option == 'g':
        cpf_completo = gerar_cpf()
        cpf_formatado = formatar_cpf(cpf_completo)
        print(cpf_formatado, end="\n\n")
    
    else:
        print("Opção inválida.")