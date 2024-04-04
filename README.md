1. El código Python descrito en el apéndice muestra cómo se cifra y se descifra un texto utilizando
DES en modo CBC. Crear un código Python que cifre y descifre tanto el texto Hola amigos de la
seguridad como el texto Hola amigas de la seguridad utilizando AES en modo CBC usando la
misma clave e IV.
Si se observa los textos cifrados, es posible ver que ese cambio de una “o” por una “a” (amigos
→ amigas) impacta en ambos textos, ¿a qué se debe ese cambio?
2. Se pide cifrar y descifrar en AES el mensaje “Hola Amigos de Seguridad” utilizando los
siguientes modos de operación:
a. ECB.
b. CTR, pasando por parámetro únicamente el campo nonce (valor aleatorio, de tamaño
(tamaño de bloque / 2)).
c. OFB, pasando por parámetro únicamente un valor IV aleatorio.
d. CFB, pasando por parámetro únicamente un valor IV aleatorio.
e. GCM, pasando como parámetros el campo nonce (valor aleatorio del mismo tamaño de
bloque) y mac_len (16).
Para más información:
https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
3. (OPCIONAL) Utilizando como base el código del apartado 1 (AES en modo CBC), crear una
clase llamada AES_CIPHER_CBC que tenga los siguientes métodos,
