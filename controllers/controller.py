from flask import render_template
from app import app
from models.order_list import order_list

@app.route('/orders')
def index():
    return render_template("index.html", title="Book shop", orders=order_list)

@app.route("/orders/<element>")
def order(element):
    return render_template("order.html", title=f"Order number {element}", current_element=order_list[int(element)])