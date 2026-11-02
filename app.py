from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        if not name or not phone:
            message = "Please enter your name and M-Pesa phone number."
        else:
            # This starter version does NOT send a real M-Pesa STK Push yet.
            # Daraja credentials and a public HTTPS callback URL are required.
            message = (
                f"Thanks, {name}! Your registration details have been received. "
                "M-Pesa payment is not connected yet. Please wait for the organiser "
                "to announce when payments are enabled."
            )
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
