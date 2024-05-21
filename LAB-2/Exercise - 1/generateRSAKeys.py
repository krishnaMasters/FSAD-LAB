from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

privateKey = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

privatePem = privateKey.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

with open("Exercise - 1/privateKey.pem", "wb") as f:
    f.write(privatePem)

publicKey = privateKey.public_key()

publicPem = publicKey.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open("Exercise - 1/publicKey.pem", "wb") as f:
    f.write(publicPem)
