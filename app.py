from flask import Flask, render_template, request, session
from buy_items import items
app = Flask(__name__)
app.secret_key = "dev2"

@app.route("/store")
def store():
        return render_template("home.html")

@app.route("/shopping", methods=["GET", "POST"])
def shopping():
# Clear shopping cart button logic
        if "money" not in session:
            session["money"] = 100

        if "shopping_cart" not in session:
            session["shopping_cart"] = []

        if "selected_item" not in session:
            session["selected_item"] = None

        if "message" not in session:
             session["message"] = ''

        if request.method == "POST":
               if request.form.get("clear_cart"):
                session["shopping_cart"] = []
                session["message"] = ""
                session["selected_item"] = None

# Making the choice buttons work
        if request.method == "POST":
                for item in items:
                    choice = request.form.get("choice")
                    if item.name.lower() == choice:
                        session["message"] = f"ITEM SELECTED: {choice}. COST OF ITEM: {item.price}"
                        session["shopping_cart"].append(choice)


# Making sure I understand how buttons work
        if request.method == "POST":
             win= request.form.get("win")
             if win: 
                  session["message"] = "I am going to win."
                  session["shopping_cart"].append("WIN")

# Getting the MONEY working
        if request.method == "POST":
             money= request.form.get("money")
             if money: 
                  session["money"] = money

        
        print("SESSION:", dict(session))
        return render_template("shopping.html", 
                               items=items,
                                selected_item=session.get("selected_item"),
                                shopping_cart=session.get("shopping_cart"),
                                message=session["message"],
                                money=session["money"]
                                )


if __name__ == "__main__":
    app.run(debug=True, port=5007)