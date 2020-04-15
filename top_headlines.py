'''
Name:
Uniqname:
'''

import secrets
import requests
from flask import Flask, render_template

API_KEY = secrets.api_key
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome!</h1>'

@app.route('/name/<nm>')
def name(nm):
    return render_template('name.html',
                    name = nm)

@app.route('/headlines/<nm>')
def headlines(nm):
    results = requests.get("https://api.nytimes.com/svc/topstories/v2/technology.json?api-key=" + API_KEY).json()['results']

    title_list = []
    for result in results[:5]:
        title_list.append(result['title'])
    
    return render_template('headlines.html',
        name = nm, headlines_list = title_list)

if __name__ == '__main__':  
    app.run(debug=True)