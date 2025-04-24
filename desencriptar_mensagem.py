from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend

# Lê a mensagem encriptada
with open("mensagem_encriptada.bin", "rb") as f:
    mensagem_encriptada = f.read()

# Carrega chave privada para desencriptar
with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())

# Desencripta a mensagem com a chave privada
mensagem_desencriptada = private_key.decrypt(
    mensagem_encriptada,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("\n📜 Mensagem desencriptada:", mensagem_desencriptada.decode())

# Lê a assinatura
with open("assinatura.bin", "rb") as f:
    assinatura = f.read()

# Carrega chave pública
with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

# Verifica assinatura
try:
    public_key.verify(
        assinatura,
        mensagem_desencriptada,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("✅ Assinatura verificada com sucesso! A mensagem é autêntica.")
except InvalidSignature:
    print("❌ Assinatura inválida! A mensagem foi alterada.")
