#funcion para validar nombres del personaje
def valid_name(msg):
    while True:
        pre_name = input(msg).title()
        if len(pre_name) >= 2:
            return pre_name
        else:
            print("Intenta con otro nombre. ")