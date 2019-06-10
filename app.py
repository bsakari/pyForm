from flask import Flask, render_template, request
import peewee

app = Flask(__name__)


@app.route('/', methods=("GET","POST"))
def form():
    if request.method == "POST":
        make = request.form["x"]
        sasa = request.form["y"]
        wewe = request.form["z"]
        # model =request.form["model"]
        # color =request.form["color"]
        # price =request.form["price"]
        items=[make, sasa,wewe]
        print(make)
        return render_template("sasa.html",items=items, make=make, sasa=sasa, wewe=wewe)

    return render_template("sasa.html")


if __name__ == '__main__':
    app.run()
