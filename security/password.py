# PWDLib
from pwdlib import PasswordHash

# Hash instance
password_hash = PasswordHash.recommended()


# Hash Password
def hash_password(password: str) -> str:
    return password_hash.hash(password)


# Verify Password
def verify_password(password: str, hashed: str) -> bool:
    return password_hash.verify(password, hashed)
