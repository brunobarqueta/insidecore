import re

def validate_passwords(password:str, confirmPass: str) -> bool:
    return password == confirmPass

def validate_fullname(fullname:str) -> bool:
    palavras = fullname.split(' ');
    return len(palavras) > 1

def validate_phone(phone:str) -> bool:
    return re.match(r'^\(?[\d]{2}\)?[ ]?[9][ ]?[\d]{4}[-]?[\d]{4}$', phone)

def validate_cpf_mask(cpf:str) -> bool:
    return re.match(r'^(\d{3}[.]){2}\d{3}-\d{2}$', cpf)

def validate_cpf(cpf:str) -> bool:
    cpf = re.sub(r'[^0-9]', '', cpf)
    
    if re.match(r'^0*$', cpf):
        return False

    if len(cpf) != 11:
        return False

    if len(set(cpf)) == 1:
        return False

    total = 0
    multiplicador = 10
    for i in range(9):
        total += int(cpf[i]) * multiplicador
        multiplicador -= 1
    resto = total % 11
    if resto < 2:
        digito_verificador1 = 0
    else:
        digito_verificador1 = 11 - resto

    total = 0
    multiplicador = 11
    for i in range(10):
        total += int(cpf[i]) * multiplicador
        multiplicador -= 1
    resto = total % 11
    if resto < 2:
        digito_verificador2 = 0
    else:
        digito_verificador2 = 11 - resto

    if int(cpf[9]) != digito_verificador1 or int(cpf[10]) != digito_verificador2:
        return False

    return True