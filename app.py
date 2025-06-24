from flask import Flask, redirect, url_for, render_template
from girls import womens
from boys import mens
from baby import kid

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/account")
def account():
    return render_template("account.html")

@app.route("/offer")
def offer():
    return render_template("offer.html",products=womens)

 

@app.route("/men")
def men():
    return render_template("men.html",products=mens)

@app.route("/men/topwear")
def topwear():
    return render_template("topwear.html",products=mens)

@app.route("/men/bottomwear")
def bottomwear():
    return render_template("bottomwear.html",products=mens)

@app.route("/men/ethnicwear")
def ethnicwear():
    return render_template("ethnicwear.html",products=mens)



@app.route("/women")
def women():
    return render_template("women.html",products=womens)

@app.route("/women/westernwear")
def westernwear():
    return render_template("westernwear.html",products=womens)

@app.route("/women/nightwear")
def gnightwear():
    return render_template("Gnightwear.html",products=womens)

@app.route("/women/ethnics")
def ethnics():
    return render_template("ethnics.html",products=womens)

@app.route("/women/accessories")
def accessories():
    return render_template("accessories.html",products=womens)



@app.route("/kids")
def kids():
    return render_template("kids.html",products=kid)

@app.route("/kids/infants")
def infants():
    return render_template("infants.html",products=kid)

@app.route("/kids/boys")
def boys():
    return render_template("boys.html",products=kid)

@app.route("/kids/girls")
def girls():
    return render_template("girls.html",products=kid)



@app.route("/women/product/<int:product_id>")
def product_detail(product_id):
    product = womens.get(product_id)
    if not product:
        return "Product not found", 404
    return render_template("product_details.html", product=product)



if __name__ == "__main__":
    app.run(debug=True)