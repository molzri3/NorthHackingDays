import jwt
import datetime

# Weak secret key
SECRET_KEY = "angeline"

# Payload with updated expiration time
payload = {
    "userName": "admin",
    "isAdmin": True,
    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)  # 30 minutes from now
}

# Generate the JWT
token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print("Generated JWT:", token)