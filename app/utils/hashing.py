import hashlib


def hash_password(password: str) -> str:
    """
    Hashes the given password using SHA256 algorithm.

    Args:
        password (str): The password to be hashed.

    Returns:
        str: The hashed password.
    """
    return hashlib.sha256(password.encode()).hexdigest()
