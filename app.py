from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient()
db = client.Contractor
contractor = db.contractor


app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage"""
    return render_template('home.html', contractor=contractor.find())

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/trucks')
def trucks():
    return render_template('trucks.html')

@app.route('/boards')
def boards():
    return render_template('boards.html')

@app.route('/wheels')
def wheels():
    return render_template('wheels.html')




# levona = [
#     { 'Levona': 'Music video' }
# ]
#
# @app.route('/levona')
# def levona_index():
#     """Return Levona mp3 page"""
#     return render_template('levona.html', levona=levona)
#
# @app.route('/new', methods=['POST'])
# def create_candy():
#     pass

if __name__ == '__main__':
    app.run(debug=True)
