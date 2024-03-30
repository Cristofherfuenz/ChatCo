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

# Función para obtener el texto original a partir de la secuencia binaria
def obtener_texto_original(secuencia_binaria):
    # Convertir la secuencia binaria a una cadena de bytes
    bytes_texto = bytearray()
    for i in range(0, len(secuencia_binaria), 8):
        byte = secuencia_binaria[i:i+8]
        bytes_texto.append(int(byte, 2))
    # Decodificar la cadena de bytes
    texto_original = bytes_texto.decode('utf-8')
    return texto_original

# Función para generar el hash SHA-512 a partir de una secuencia binaria
def generar_hash_sha512(secuencia_binaria):
    return hashlib.sha512(secuencia_binaria.encode()).hexdigest()

# Función para generar el hash SHA-256 a partir de un hash SHA-512
def generar_hash_sha256(hash_sha512):
    return hashlib.sha256(hash_sha512.encode()).hexdigest()

# Datos de la prueba número 1
texto_original = "hola mundo"
secuencia_binaria_esperada = "01101000011011110110110001100001001000000110110101110101011011100110010001101111"
secuencia_aritmetica_esperada = [4, 48, 48, 12, 240, 4, 12, 12, 12, 240, 16, 12, 48, 240, 240, 16, 12, 48, 240, 20, 16, 48, 12, 12, 20, 16, 48, 12, 12, 20, 4, 48, 12, 12, 240, 4, 12, 12, 12, 20, 4, 48, 48, 12, 240, 16, 12, 48, 12, 240, 16, 48, 12, 240, 20, 16, 12, 48, 240, 20, 16, 48, 48, 12, 20, 16, 48, 12, 12, 240, 4, 12, 12, 240, 240, 4, 48, 48, 240, 240]
hash_sha512_esperado = "5a2b1e655d5fadcfcd76131aa874b1593ea713aee2b4d77c6c49c4b05d868b4632699638dfda657cd0c9cdac9c0be178e6ccc336a5eed2563321bf9e3956d732"
hash_sha256_esperado = "d995631ac239304ff7284f50e34dd32b420d345be7651311c3c32b5135fae750"

# Convertir la secuencia aritmética a una secuencia binaria
secuencia_binaria_calculada = convertir_a_binario(secuencia_aritmetica_esperada)

# Verificar si la secuencia binaria calculada coincide con la esperada
if secuencia_binaria_calculada == secuencia_binaria_esperada:
    print("La secuencia binaria calculada coincide con la esperada.")
else:
    print("La secuencia binaria calculada no coincide con la esperada.")

# Obtener el texto original a partir de la secuencia binaria
texto_original_calculado = obtener_texto_original(secuencia_binaria_calculada)

# Verificar si el texto original calculado coincide con el esperado
if texto_original_calculado == texto_original:
    print("El texto original calculado coincide con el esperado.")
else:
    print("El texto original calculado no coincide con el esperado.")

# Generar el hash SHA-512 a partir de la secuencia binaria
hash_sha512_calculado = generar_hash_sha512(secuencia_binaria_esperada)

# Verificar si el hash SHA-512 calculado coincide con el esperado
if hash_sha512_calculado == hash_sha512_esperado:
    print("El hash SHA-512 calculado coincide con el esperado.")
else:
    print("El hash SHA-512 calculado no coincide con el esperado.")

# Generar el hash SHA-256 a partir del hash SHA-512
hash_sha256_calculado = generar_hash_sha256(hash_sha512_calculado)

# Verificar si el hash SHA-256 calculado coincide con el esperado
if hash_sha256_calculado == hash_sha256_esperado:
    print("El hash SHA-256 calculado coincide con el esperado.")
else:
    print("El hash SHA-256 calculado no coincide con el esperado.")
