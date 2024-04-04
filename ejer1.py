from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Datos necesarios
key = get_random_bytes(16)  # Clave aleatoria de 128 bits para AES
nonce = get_random_bytes(16)  # Valor aleatorio para el nonce en modo EAX
data = "Hola amigas de seguridad".encode("utf-8")  # Datos a cifrar
print(data)

# CIFRADO ##########################################################################

# Creamos un mecanismo de cifrado AES en modo EAX con un valor de nonce
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

# Ciframos, haciendo que la variable “data” sea múltiplo del tamaño de bloque
ciphertext, tag = cipher.encrypt_and_digest(pad(data, AES.block_size))

# Mostramos el cifrado por pantalla en modo binario
print(ciphertext)

# DESCIFRADO #######################################################################

# Creamos un mecanismo de (des)cifrado AES en modo EAX con el mismo valor de nonce
# Ambos, cifrado y descifrado, se crean de la misma forma
decipher_aes = AES.new(key, AES.MODE_EAX, nonce=nonce)

# Desciframos, eliminamos el padding, y recuperamos la cadena
new_data = unpad(decipher_aes.decrypt(ciphertext), AES.block_size).decode("utf-8", "ignore")

# Imprimimos los datos descifrados
print(new_data)
