import json
import base64

# Create an admin user
user_data = {"userName": "admin", "isAdmin": True}

# Encode to Base64
cookie_value = base64.b64encode(json.dumps(user_data).encode()).decode()

print(cookie_value)
