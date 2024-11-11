from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


# JSON
def read_json():
    with open('products.json') as file:
        return json.load(file)


# CSV
def read_csv():
    products = []
    with open('products.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(row)
    return products


# SQL
def read_sqlite():
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute('SELECT * FROM products')
    products = c.fetchall()
    conn.close()

    product_list = [
        {'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]}
        for row in products
    ]
    return product_list




@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []

    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sqlite()
    else:
        return render_template(
            'product_display.html',
            error="Wrong source")

    if product_id:
        products = \
            [p for p in products if str(p.get('id')) == product_id]
        if not products:
            return render_template(
                'product_display.html',
                error="Product not found")

    return render_template(
        'product_display.html',
        products=products)


if __name__ == '__main__':
    app.run(debug=True)