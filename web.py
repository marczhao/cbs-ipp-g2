from flask import Flask, render_template, request
from googlefinance import getQuotes
import os
import giphypop
g = giphypop.Giphy()
app = Flask(__name__)

@app.route('/')
def index():
    greeting = "Hello, Fellow Consultants!"
    return render_template('index.html', greeting=greeting)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/results')
def results():
    results = g.search(request.values.get('keywords'))
    return render_template('results.html', results=results)

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)