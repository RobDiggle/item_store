from flask import Flask, render_template, request, session
from buy_items import items, item_choice_made, purchase_choice_made, money

app = Flask(__name__)
app.secret_key = "dev2"


@app.route("/store")
def store():
        return render_template("home.html")

@app.route("/shopping", methods=["GET", "POST"])
def shopping():
        if "money" not in session:
            session["money"] = 100

        if "shopping_cart" not in session:
            session["shopping_cart"] = []

        if "selected_item" not in session:
            session["selected_item"] = None

        
        # if you cut out the next  line then local variable message is not associated with a value
        message = 'CLICK ON A BUTTON TO LEARN ABOUT THE PRODUCT'
        purchase_message = session.get("purchase_message", "")

        if request.method == "POST":
               if request.form.get("clear_cart"):
                session["shopping_cart"] = []
                session["purchase_message"] = ""
                session["selected_item"] = None

               choice = request.form.get("choice")
               if choice:
                    session["selected_item"] = choice
                    message = item_choice_made(choice)

               purchase_choice = request.form.get("purchase_choice") 
               if purchase_choice: # and money >= item.price:
                        print("SELECTED ITEM FROM SESSION:", session.get("selected_item"))
                        #session["money"] -= item.price
                        session["shopping_cart"].append(session["selected_item"])
                        message = ''
                        session["purchase_message"] = purchase_choice_made(purchase_choice)

        print("SESSION:", dict(session))
        return render_template("shopping.html", 
                               items=items, message=message, 
                               purchase_message=purchase_message,
                                selected_item=session.get("selected_item"),
                                shopping_cart=session.get("shopping_cart"))


if __name__ == "__main__":
    app.run(debug=True, port=5007)
