import json
import base64
from flask import Flask, request, make_response

flag = "NHD{be_cautious_when_serializing_and_deserializing}"

class User:
    def __init__(self, userName, isAdmin):
        self.userName = userName
        self.isAdmin = isAdmin

def serialize_user(user):
    """Convert User object to JSON and encode it in Base64."""
    user_dict = {"userName": user.userName, "isAdmin": user.isAdmin}
    json_data = json.dumps(user_dict).encode()
    return base64.b64encode(json_data).decode()

def deserialize_user(data):
    """Decode Base64 and parse JSON into a User object."""
    try:
        user_dict = json.loads(base64.b64decode(data).decode())
        return User(user_dict["userName"], user_dict["isAdmin"])
    except Exception:
        return None

app = Flask(__name__)

@app.route('/')
def index():
    user_cookie = request.cookies.get('user')
    if not user_cookie:
        user = User("anonymous", False)
        resp = make_response("Welcome, anonymous!")
        resp.set_cookie('user', serialize_user(user))
        return resp
    
    user = deserialize_user(user_cookie)
    if user and isinstance(user, User):
        if user.userName == "admin" and user.isAdmin:
            return f"Congrats! You've solved the challenge.<br> Here is your flag: {flag}"
        return f"Hello, {user.userName}. You are not an admin."
    
    return "Invalid cookie. Try again."

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
