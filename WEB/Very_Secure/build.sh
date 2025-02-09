docker build -t flask_insecure .
docker run -d -p 5000:5000 --name flask_insecure_container flask_insecure