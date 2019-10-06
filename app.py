from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage"""
    return render_template('home.html', msg='Music')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/comp')
def comp():
    return render_template('comp.html')

@app.route('/levona')
def levona():
    return render_template('levona.html')



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
