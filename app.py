from flask import Flask, render_template, request
from buy_items import items, item_choice_made, purchase_choice_made

app = Flask(__name__)

@app.route("/store")
def store():
        return render_template("home.html")

@app.route("/shopping", methods=["GET", "POST"])
def shopping():
        # if you cut out the next  line then local variable message is not associated with a value
        message = 'CLICK ON A BUTTON TO LEARN ABOUT THE PRODUCT'
        purchase_message = ''

        if request.method == "POST":
               choice = request.form.get("choice") 
               message = item_choice_made(choice)
               purchase_choice = request.form.get("purchase_choice") 
               purchase_message = purchase_choice_made(purchase_choice)

        return render_template("shopping.html", items=items, message=message, purchase_message=purchase_message)


if __name__ == "__main__":
    app.run(debug=True, port=5007)
