import jwt
from cryptography.hazmat.primitives import serialization
import os
from dotenv import load_dotenv

load_dotenv()


def decodeToken(token, algorithms, secretKey = os.getenv('JWT_SECRET')):
    if algorithms == ['RS256']:
        with open("Exercise - 1/publicKey.pem", "rb") as f:
            publicKey = serialization.load_pem_public_key(
                f.read()
            )
        secretKey = publicKey
    try:
        decoded = jwt.decode(token, secretKey, algorithms)
        print("Decoded " + algorithms[0] + " token: ")
        print(decoded)
    except jwt.exceptions.PyJWTError as e:
        print("Invalid JWT:", e)


tokenWithRS256 = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InZpdmFuMjQyMCIsInVzZXJJRCI6NzQ2LCJkb21haW4iOiJjb21wdXRlciBzY2llbmNlIiwicm9sZSI6InVzZXIiLCJwZXJtaXNzaW9uIjoidXNlciBhY2Nlc3MiLCJleHAiOjE3MTYyODkwNTR9.ROAZf_CNv_LerDxxjDVmPUd5oWx4eHmYWnhN_eoUizKk7oBsmRQIi0dGY6lZP2BPgNcDOB9nConq7vbLgfgNiEeSLVjTUyuwZpokXqgt03i0MClXr4DnqymHPl-6bVQZJbrT6CEaH4oheA-3AUUJvTKac_llcHv5Th9Trju3GghhlbMVhxosngExkFNCdLc2FiT6NWkUOpc6bUwh9ZKFSgyp5maFMi_cjSKoms7y5Qg429j7zKbi23d24U1fW-TrErwy5LITKKbwV-6qrbysh6Jq_hrA_GdQe5CA-Ho4T5pfCn_6olnJS5Eye8LEgFxJg-DeKTY8B6hcdeNqKaxsLg"
tokenWithHS256 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InZpdmFuMjQyMCIsInVzZXJJRCI6NzQ2LCJkb21haW4iOiJjb21wdXRlciBzY2llbmNlIiwicm9sZSI6InVzZXIiLCJwZXJtaXNzaW9uIjoidXNlciBhY2Nlc3MiLCJleHAiOjE3MTYyODkwNTR9.sPbxPZUBjOpiPjQwd_8fvLg9Q4c4bonHyh55vrouJu8"

decodeToken(tokenWithRS256, ['RS256'])
decodeToken(tokenWithHS256, ['HS256'])


