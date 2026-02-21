def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a
 
def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
 
def inverso_modular(e, z):
    t, t2 = 0, 1
    r, r2 = z, e
    while r2 != 0:
        res = r // r2
        t, t2 = t2, t - res * t2
        r, r2 = r2, r - res * r2
    if r > 1:
        raise Exception("e não possui inverso modular")
    if t < 0:
        t = t + z
    return t

def criptografar(mensagem, chave_publica):
    e, n = chave_publica
    mensagem_bytes = mensagem.encode('latin-1')  # Transforma a mensagem para bytes e então codifica a mensagem para cada caractere equivalente ao byte da mensagem
    return [pow(byte, e, n) for byte in mensagem_bytes] # Elevo cada caractere da mensagem por E modulo N para criptografar
 
def descriptografar(mensagem_cripto, chave_privada):
    d, n = chave_privada
    bytes_decifrados = []
    for c in mensagem_cripto:
        decifrado = pow(c, d, n) # Verificamos se o numero está entre 0 e 255, caso não seja verdade nós forçamos ele a estar com a linha abaixo.
        byte_valido = decifrado % 256  # Isso garante que o valor fique entre 0 e 255
        bytes_decifrados.append(byte_valido)
    return bytes(bytes_decifrados).decode('latin-1', errors='replace') # Fazemos o efeito reverso, pegando a mensagem que agora é uma lista de bytes e transformando em uma string
       
# Gerar chaves
while True:
    try:
        p = 500113
        q = 500119
        if primo(p) and primo(q) and p != q:
            break
        else:
            print("Erro: p e q devem ser primos diferentes.")
    except ValueError:
        print("Digite apenas números inteiros.")
 
n = p * q
z = (p - 1) * (q - 1)
 
# Escolhe um valor de e válido
for e in range(3, z):
    if mdc(e, z) == 1:
        break
 
# Calcula d
d = inverso_modular(e, z)
 
print("\nChave Pública (e, n):", (e, n))
print("Chave Privada (d, n):", (d, n))
 
mensagem_input = input("\nDigite a mensagem para criptografar: ")
 
# Criptografa
mensagem_cripto = criptografar(mensagem_input, (e, n))
print("\nMensagem criptografada:")
print(mensagem_cripto)
 
entrada_d = int(input("\nDigite o valor de d da chave privada: "))
entrada_n = int(input("Digite o valor de n da chave privada: "))
msg_limpa = [int(num) for num in mensagem_cripto]
 
 
msg_limpa = input("Digite a mensagem para ser descriptografada: ")
msg_limpa = msg_limpa.strip('[]').replace(' ', '')
msg_limpa = msg_limpa.split(',')
msg_limpa = [int (num) for num in msg_limpa]
 
# Descriptografa
mensagem_original = descriptografar(msg_limpa, (entrada_d, entrada_n))
print("\nMensagem descriptografada:")
print(mensagem_original)