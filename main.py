from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/contacts.html")
# def contacts():
#     return render_template("contacts.html")

if __name__ == "__main__":
    app.run(debug=True)