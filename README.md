# Projeto de Encriptação e Assinatura Digital com RSA 🔒✍️

Este projeto implementa a encriptação e assinatura digital utilizando o algoritmo RSA. Ele permite gerar chaves públicas e privadas, encriptar uma mensagem, assinar digitalmente a mensagem encriptada com a chave privada e verificar a assinatura com a chave pública.

## Funcionalidades 🛠️

1. **Geração de Chaves RSA** 🔑: Gera uma chave pública e uma chave privada para uso na encriptação e assinatura digital.
2. **Encriptação de Mensagem** 🔐: Encripta uma mensagem usando a chave pública.
3. **Assinatura Digital** ✍️: Assina a mensagem encriptada com a chave privada.
4. **Desencriptação de Mensagem** 🔓: Desencripta a mensagem usando a chave privada.
5. **Verificação de Assinatura** ✅: Verifica a assinatura digital usando a chave pública.

## Estrutura do Projeto 📁

- `gerar_chaves.py`: Gera e salva as chaves RSA (pública e privada).
- `encriptar_mensagem.py`: Encripta uma mensagem e gera a assinatura digital com a chave privada.
- `desencriptar_mensagem.py`: Desencripta a mensagem e verifica a assinatura digital usando a chave pública.
- `mensagem.txt`: Arquivo de exemplo com uma mensagem a ser encriptada e assinada.

## Como Usar 🚀

### 1. Geração das Chaves RSA 🔑
Execute o script `gerar_chaves.py` para gerar as chaves públicas e privadas. Isso criará dois arquivos: `private_key.pem` e `public_key.pem`.

```bash
python gerar_chaves.py

