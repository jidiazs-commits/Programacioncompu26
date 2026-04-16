# Fumcion para convertir vistas en numeros
def convertir(valor_str):
   
    valor_str = valor_str.strip().upper() #quita los espacios en blanco y lo pone en mayusculas 
    
    #como el valor es un string se pone esta condicion para regresar un float y poderlo utilizar
    if valor_str == '' or valor_str == '0':
        return 0.0
    #defini esta variable para poder pasar los numeros a float
    multiplicador = 1
    
    #se revisa con qué letra termina y se le asigna el multiplicador para dejar el numero plano
    if valor_str.endswith('B'): #si termina con B
        multiplicador = 1000000000
    #corte el texto para quitar la última letra '16.8B'='16.8'
        valor_str = valor_str[:-1] 
    elif valor_str.endswith('M'):
        multiplicador = 1000000
        valor_str = valor_str[:-1]
    elif valor_str.endswith('K'):
        multiplicador = 1000
        valor_str = valor_str[:-1]
        
    #converti el texto a decimal y lo multiplicamos
    #defini la variable para que pase de str a float y se multiplique por el valor correspondiente segun su letra 
    valor_final = float(valor_str) * multiplicador
    return valor_final