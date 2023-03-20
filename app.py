from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/login")
def login():
    user = request.args.get("user")
    password = request.args.get("password")
    if user == "admin" and password == "xxx123##":
        return render_template("login.html", user = user, password = password)
    else:
        return render_template("nonlogin.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)