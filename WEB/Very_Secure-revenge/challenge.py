import jwt
import datetime
import json
from flask import Flask, request, make_response, render_template

SECRET_KEY = "angeline"  # Weak secret, easy to brute-force
FLAG = "NHD{be_cautious_when_using_weak_jwt_secrets}"

class User:
    def __init__(self, userName, isAdmin):
        self.userName = userName
        self.isAdmin = isAdmin

def generate_token(user):
    """Generate a JWT token with user details."""
    payload = {
        "userName": user.userName,
        "isAdmin": user.isAdmin,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_token(token):
    """Decode and verify JWT token."""
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return User(decoded["userName"], decoded["isAdmin"])
    except jwt.ExpiredSignatureError:
        return None  # Expired token
    except jwt.InvalidTokenError:
        return None  # Invalid token

app = Flask(__name__)

@app.route('/')
def index():
    user_cookie = request.cookies.get('user')
    
    if not user_cookie:
        # Default anonymous user
        user = User("anonymous", False)
        token = generate_token(user)  # Generate JWT token
        resp = make_response(render_template("index.html", user="anonymous", is_admin=False))
        resp.set_cookie('user', token)  # Store JWT in cookie
        return resp

    user = decode_token(user_cookie)  # Decode JWT token
    if user and isinstance(user, User):
        return render_template("index.html", user=user.userName, is_admin=user.isAdmin, flag=FLAG if user.isAdmin else None)

    return "Invalid or expired token. Try again."

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
