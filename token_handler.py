import time
import hmac
import hashlib
import base64

SECRET_KEY = b"your-strong-secret-key"

def generate_token(domain: str, email: str, ttl_seconds: int = 86400) -> str:
    timestamp = int(time.time())
    expires = timestamp + ttl_seconds
    email_hash = hashlib.sha256(email.encode()).hexdigest()
    
    raw = f"{domain}|{email_hash}|{expires}"
    signature = hmac.new(SECRET_KEY, raw.encode(), hashlib.sha256).hexdigest()
    
    token = f"{raw}|{signature}"
    return base64.urlsafe_b64encode(token.encode()).decode()
