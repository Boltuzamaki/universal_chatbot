import hashlib

def hash_password(password: str) -> str:
    """
    Hashes the given password using SHA256 algorithm.
    """
    return hashlib.sha256(password.encode()).hexdigest()