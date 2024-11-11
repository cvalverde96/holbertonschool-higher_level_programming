from flask import Flask, render_template, request
import json
import csv

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


@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []

    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
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