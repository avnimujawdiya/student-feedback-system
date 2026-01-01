from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    subject = request.form["subject"]
    rating = request.form["rating"]
    feedback = request.form["feedback"]

    with open("feedback.txt", "a") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Subject: {subject}\n")
        file.write(f"Rating: {rating}\n")
        file.write(f"Feedback: {feedback}\n")
        file.write("-" * 30 + "\n")

    return "Feedback submitted successfully!"

if __name__ == "__main__":
    app.run(debug=True)
