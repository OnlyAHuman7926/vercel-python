# wsgi.py
from main import mmian

if __name__ == "__main__":
    print("thing")
    mmian.run(host="0.0.0.0", port=8080)
else:
    print("application = mmian")
    application = mmian
