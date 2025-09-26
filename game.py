from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

choices = ["stone", "paper", "scissor"]

@app.route("/")
def home():
    return render_template("spsgame.html")

@app.route("/play", methods=["POST"])
def play():
    user_choice = request.json["choice"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "draw"
    elif (user_choice == "stone" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "stone") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        result = "win"
    else:
        result = "lose"

    return jsonify({"user": user_choice, "computer": computer_choice, "result": result})

if __name__ == "__main__":
    app.run(debug=True)
