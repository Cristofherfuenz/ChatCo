import sqlite3
import hashlib
import numpy as np

# Función para generar una secuencia binaria a partir de una cadena de texto
def generar_secuencia_binaria(texto):
    # Convertir el texto a una secuencia de bytes
    bytes_texto = bytes(texto, 'utf-8')
    # Generar la secuencia binaria a partir de los bytes
    return ''.join(format(byte, '08b') for byte in bytes_texto)

# Función para convertir la secuencia binaria a una secuencia aritmética
def convertir_a_aritmetica(secuencia_binaria):
    aristas = [4, 12, 12, 12, 20]  # Números de aristas de los sólidos platónicos: tetraedro, hexaedro, octaedro, dodecaedro, icosaedro
    caras = [4, 6, 8, 12, 20]  # Números de caras
    vertices = [4, 8, 6, 20, 12]  # Números de vértices

    aritmetica = []
    i = 0
    while len(aritmetica) < len(secuencia_binaria):
        if secuencia_binaria[i] == '0':
            aritmetica.append(aristas[i % len(aristas)])
        else:
            aritmetica.append(caras[i % len(caras)] * vertices[i % len(vertices)])
        i += 1
    return aritmetica

# Función para generar el hash SHA-512 a partir de una secuencia binaria
def generar_hash_sha512(secuencia_binaria):
    return hashlib.sha512(secuencia_binaria.encode()).hexdigest()

# Función para generar el hash SHA-256 a partir de un hash SHA-512
def generar_hash_sha256(hash_sha512):
    return hashlib.sha256(hash_sha512.encode()).hexdigest()

# Establecer conexión con la base de datos SQLite
conexion = sqlite3.connect('data-base-2.db')
cursor = conexion.cursor()

# Crear tabla para almacenar los datos si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS datos (
                    id INTEGER PRIMARY KEY,
                    texto_original TEXT,
                    secuencia_binaria TEXT,
                    secuencia_aritmetica TEXT,
                    hash_sha512 TEXT,
                    hash_sha256 TEXT)''')

# Solicitar al usuario que ingrese una palabra o frase
texto_original = "hola mun2"

# Generar secuencia binaria, secuencia aritmética y hashes
secuencia_binaria = generar_secuencia_binaria(texto_original)
secuencia_aritmetica = convertir_a_aritmetica(secuencia_binaria)
hash_sha512_madre = generar_hash_sha512(secuencia_binaria)
hash_sha256_madre = generar_hash_sha256(hash_sha512_madre)

# Insertar los datos en la base de datos
cursor.execute("INSERT INTO datos (texto_original, secuencia_binaria, secuencia_aritmetica, hash_sha512, hash_sha256) VALUES (?, ?, ?, ?, ?)", 
               (texto_original, secuencia_binaria, str(secuencia_aritmetica), hash_sha512_madre, hash_sha256_madre))

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()

print("Se han generado y almacenado los datos y hashes en la base de datos SQLite.")
