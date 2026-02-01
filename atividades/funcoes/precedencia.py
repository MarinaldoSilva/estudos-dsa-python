def pode_entrar(is_vip, has_ticket, age):
    if (is_vip or has_ticket and age >= 18):
        return True
    return False

print(pode_entrar(True, False, 17))
