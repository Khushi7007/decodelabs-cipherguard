from flask import Flask, render_template, request
from cipher import encrypt, decrypt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def home():

    encrypted = ""
    decrypted = ""

    if request.method == "POST":

        text = request.form["text"]
        shift = int(request.form["shift"])

        encrypted = encrypt(text, shift)
        decrypted = decrypt(encrypted, shift)

    return render_template(
        "index.html",
        encrypted=encrypted,
        decrypted=decrypted
    )

if __name__ == "__main__":
    app.run(debug=True,port=5003)
