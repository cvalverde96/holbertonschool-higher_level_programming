from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items')
def items():
    # Read data from items.json
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            items_list = data.get("items", [])  # Get the "items" list, default to empty list if not found
    except FileNotFoundError:
        items_list = []  # If the file doesn't exist, default to an empty list
    except json.JSONDecodeError:
        items_list = []  # If there's an error in the JSON file, default to an empty list

    # Pass the items list to the template
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
