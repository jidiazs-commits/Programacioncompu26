def convertir(valor_str):
   
    valor_str = valor_str.strip().upper() #quita los espacios en blanco y lo pone en mayusculas 
    
    #como el valor es un string se pone esta condicion para regresar un float y poderlo utilizar
    if valor_str == '' or valor_str == '0':
        return 0.0
    #defini esta variable para poder pasar los numeros a float
    multiplicador = 1
    
    #se revisa con que letra termina y se le asigna el multiplicador para dejar el número plano
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
    #Falto un bloque try-except para que no colapse si hay un texto que no es legible
    try:
        valor_final = float(valor_str) * multiplicador
        return valor_final
    except ValueError:
        return 0.0
        
#Función principal para calcular
def procesar_estadisticas_vistas(ruta_archivo):
    # 
    # Cree las variables acumuladoras para guardar el número más alto, el más bajo y la suma de todos y el contador para saber cuántas filas proceso.
    max_val_vistas = 0.0
    min_val_vistas = 0.0
    sumatoria_vistas = 0.0
    
    #Cree las variables de estado para los likes y los nombres de los videos.
    max_val_likes = 0.0
    min_val_likes = 0.0
    sumatoria_likes = 0.0
    nombre_max_vistas = ""
    nombre_min_vistas = ""
    nombre_max_likes = ""
    nombre_min_likes = ""
    # Identifique el encabezado(primer fila) que son los titulos y estos no se procesan como números
    es_encabezado = True
    # Hice esto para que el primer número procesado se convierta en el primer mínimo y el primer máximo
    es_primer_dato = True
    
    # Abri el archivo de forma normal
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        
        # Procesa el archivo línea por línea
        for linea in archivo:
            
            # Si es la primera línea se cambia a false y el continue funciona para saltasr el resto del codigo y pasar a la siguiente línea que son los datos reales
            if es_encabezado == True:
                es_encabezado = False
                continue
            linea = linea.strip() #aqui selimpia la línea de saltos invisibles (\n) antes de cortarla
            # Corta la línea de texto cada vez que encuentra una coma y lo convierte a una lista de palabras
            columnas = linea.split(',')
            # Valido que la fila no este rota o vacia para que no de error
            if len(columnas) < 9:
                continue
            nombre_video = columnas[1]#accede a la última columna para los likes
            vistas_str = columnas[-2]# Accede a la penultima columna
            likes_str = columnas[-1]
            #Llama a la función de transformar el texto a un número
            valor_numerico_vistas = convertir(vistas_str)
            valor_numerico_likes = convertir(likes_str)
            ##Ahi cree la condicion que faltaba para qeu el primer numero es el mas grande y el mas pequeño de los numeros
            if es_primer_dato == True:
                # Si es el primer dato que se lee, es el mayor y el menor a la vez
                max_val = valor_numerico_vistas
                min_val = valor_numerico_vistas
                es_primer_dato = False ##Esto es porque como la fila tiene los titulos de las columnas pues no se pueden procesar ni nos interesa que se procese
            else:
                # y sii no es el primero, se compara con los que ya se tienen guardados
                if valor_numerico_vistas > max_val:
                    max_val = valor_numerico_vistas
                    
                if valor_numerico_vistas < min_val:
                    min_val = valor_numerico_vistas
            
            #Suma el valor actual al total que ya esta acomulado y se suma 1 al contador de registros.
            sumatoria = sumatoria + valor_numerico_vistas
            contador = contador + 1
            
    # Se divide la suma total entre el número de filas procesadas
    promedio = 0.0
    if contador > 0:
        promedio = sumatoria / contador
        
    # Envia los cuatro resultados finalaes listos para usarlos fuera de la función
    return max_val, min_val, promedio, contador
    #Ya esta el contador, el promedioo el return que envia los resultados finales.a
    #Unicamente falta la parte de ellos y hacer la interfaz