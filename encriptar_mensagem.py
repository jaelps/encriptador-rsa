from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

# Caminho do arquivo da mensagem
caminho_arquivo = "mensagem.txt"

# Lê o conteúdo do arquivo
with open(caminho_arquivo, "rb") as f:
    mensagem = f.read()

# Carrega chave pública
with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read(), backend=default_backend())

# Encripta a mensagem com a chave pública
mensagem_encriptada = public_key.encrypt(
    mensagem,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Carrega chave privada para assinar
with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())

# Assina a mensagem original com a chave privada
assinatura = private_key.sign(
    mensagem,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Salva a mensagem encriptada
with open("mensagem_encriptada.bin", "wb") as f:
    f.write(mensagem_encriptada)

# Salva a assinatura
with open("assinatura.bin", "wb") as f:
    f.write(assinatura)

print("🔒 Mensagem encriptada e assinatura gerada com sucesso!")
