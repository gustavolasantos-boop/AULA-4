#LOGICA E (and)
verifica_email = True
verifica_senha = False

login = verifica_email and verifica_senha
print(login)

if login:
    print("Entrar no programa")

#LOGICA OU (or)
logica_ou = False or False or True
print(logica_ou)

#NEGAÇÃO
negação = not False
print(negação)

if not login:
    print("Loga certo ae")