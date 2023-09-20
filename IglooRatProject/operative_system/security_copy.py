# quiero que me generes un codigo que utilice python para crear copias de seguridad de una carpeta 
# especifica en mi computadora y que al finalizar se imprima por consola un mensaje de que la copia de 
# seguridad fue realizada

'''
Here is an example of how you can create a Python script to perform backup tasks on your computer, 
in this case backing up a specific folder on your system:
''' 

# Import the neccessary libraries
import shutil
import os
import time

# Source Directory (files to backup)
source = "C:/Users/Gonza/Desktop/recibos"

# Destiny directory (where we are saving the security copy)
destination = "C:/Users/Gonza/Desktop/security_copy"

# Obtaining the actual date time
current_date = time.strftime('%Y-%m-%d')

# Creata a folder with the actual date as name
destination_directory = os.path.join(destination, current_date)

try: 
    # Create a destiny folder if it doesn't exist
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # List files in source directory
    files = os.listdir(source)

    # Copiar cada archivo al directorio de destino
    for file in files:
        source_file = os.path.join(source, file)
        destination_file = os.path.join(destination_directory, file)
        shutil.copy(source_file, destination_file)

    print(f'Copia de seguridad realizada en {destination_directory}')
except Exception as e:
    print(f"An error occurred during backup execution : {e}")


# Outpout: 

'''

'''

# como puedo lograr que esta copia de seguridad sea relizada semanalmente y que el script tenga permisos de administrador
# para realizar la tarea


'''

'''

import schedule
import shutil
import os
import time

# Directorio de origen (archivos a respaldar)
origen = "C:/Users/Gonza/Desktop/recibos"

# Directorio de destino (donde se guardarán las copias de seguridad)
destino = "C:/Users/Gonza/Desktop/security_copy"

# Obtener la fecha actual
fecha_actual = time.strftime('%Y-%m-%d')

# Crear una carpeta con la fecha actual como nombre
carpeta_destino = os.path.join(destino, fecha_actual)

# Función para realizar la copia de seguridad
def realizar_copia_de_seguridad():
    # Obtener la fecha actual
    fecha_actual = time.strftime('%Y-%m-%d')

    # Crear una carpeta con la fecha actual como nombre
    carpeta_destino = os.path.join(destino, fecha_actual)

    # Crear la carpeta de destino si no existe
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Listar archivos en el directorio de origen
    archivos = os.listdir(origen)

    # Copiar cada archivo al directorio de destino
    for archivo in archivos:
        origen_archivo = os.path.join(origen, archivo)
        destino_archivo = os.path.join(carpeta_destino, archivo)
        shutil.copy(origen_archivo, destino_archivo)

    print(f'Copia de seguridad realizada en {carpeta_destino}')

try: 
    # Programar la copia de seguridad para ejecutarse todos los días a la misma hora
    schedule.every().day.at('08:00').do(realizar_copia_de_seguridad)

    # Bucle principal para mantener el programa en ejecución
    while True:
        schedule.run_pending()
        time.sleep(1)

except Exception as e:
    print(f"Ocurrió un error al realizar la copia de seguridad: {e}")


# Output:
'''

'''

'''

'''

# como puedo hacer para que mi script se ejecute automaticamente al encender mi computadora ?

import os
import getpass
import winreg as reg

# Ruta completa al script que deseas ejecutar al inicio
ruta_script = r'C:/Ruta/Completa/Al/Script/mi_script.py'

# Nombre de la entrada en el registro
nombre_entrada = 'MiScriptAlInicio'

# Obtén el nombre de usuario actual
usuario_actual = getpass.getuser()

# Ruta al registro de ejecución al inicio
ruta_registro = r'Software/Microsoft/Windows/CurrentVersion/Run'

# Ruta completa al registro
ruta_completa_registro = f'HKEY_CURRENT_USER\\{ruta_registro}'

# Intenta agregar la entrada en el registro
try:
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, ruta_registro, 0, reg.KEY_WRITE)
    reg.SetValueEx(key, nombre_entrada, 0, reg.REG_SZ, ruta_script)
    reg.CloseKey(key)
    print(f'Se ha agregado la entrada "{nombre_entrada}" en el registro.')
except Exception as e:
    print(f'Error al agregar la entrada en el registro: {str(e)}')
