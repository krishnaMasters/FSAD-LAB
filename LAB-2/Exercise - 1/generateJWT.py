import jwt
import time
from cryptography.hazmat.primitives import serialization
import os
from dotenv import load_dotenv

load_dotenv()

def generateToken(payload, algorithm):
    if algorithm == 'HS256':
        secretKey = os.getenv('JWT_SECRET')
        return jwt.encode(payload, secretKey, algorithm)
    else:
        with open("Exercise - 1/privateKey.pem", "rb") as f:
            privateKey = serialization.load_pem_private_key(
                f.read(),
                password=None,
            )
        return jwt.encode(payload, privateKey, algorithm)


payload = {
    "username": "vivan2420",
    "userID": 746,
    "domain": "computer science",
    "role": "user",
    "permission": "user access",
    "exp": int(time.time()) + 60 * 60  
}


tokenWithHS256 = generateToken(payload, 'HS256')
tokenWithRS256 = generateToken(payload, 'RS256')

print("Token generated via HS256 = " + tokenWithHS256)
print("Token generated via RS256 = " + tokenWithRS256)

