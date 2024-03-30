import sqlite3
import hashlib

# Función para convertir la secuencia aritmética a una secuencia binaria
def convertir_a_binario(secuencia_aritmetica):
    aristas = [4, 12, 12, 12, 20]  # Números de aristas de los sólidos platónicos: tetraedro, hexaedro, octaedro, dodecaedro, icosaedro
    caras = [4, 6, 8, 12, 20]  # Números de caras
    vertices = [4, 8, 6, 20, 12]  # Números de vértices

    secuencia_binaria = ""
    for item in secuencia_aritmetica:
        if item in aristas:
            secuencia_binaria += '0'
        else:
            secuencia_binaria += '1'
    return secuencia_binaria

# Función para obtener el texto original a partir del hash SHA-256
def obtener_texto_original(hash_sha256):
    conexion = sqlite3.connect('data-base-2.db')
    cursor = conexion.cursor()

    # Buscar el texto original correspondiente al hash SHA-256 en la base de datos
    cursor.execute("SELECT texto_original FROM datos WHERE hash_sha256=?", (hash_sha256,))
    resultado = cursor.fetchone()

    conexion.close()

    if resultado:
        return resultado[0]  # Devuelve el texto original si se encuentra en la base de datos
    else:
        return None  # Devuelve None si no se encuentra en la base de datos

# Función para generar el hash SHA-256 a partir de un hash SHA-512
def generar_hash_sha256(hash_sha512):
    return hashlib.sha256(hash_sha512.encode()).hexdigest()

# Ingresar el hash SHA-256
hash_sha256_ingresado = "8ba0d9515c9c84736037072f0ded252a9d55e15b7a48f2988fbbcbb827025b74"

# Obtener el hash SHA-512 a partir del hash SHA-256 ingresado
hash_sha512_calculado = generar_hash_sha256(hash_sha256_ingresado)

# Buscar el texto original correspondiente al hash SHA-256 en la base de datos
texto_original = obtener_texto_original(hash_sha256_ingresado)

if texto_original:
    print("El mensaje en lenguaje natural correspondiente al hash ingresado es:")
    print(texto_original)
else:
    print("El hash ingresado no corresponde a ningún mensaje en la base de datos.")
