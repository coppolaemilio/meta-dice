import flask
import string
import random
app = flask.Flask(__name__)

def id_generator(size=20, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@app.route('/')
def index():
    return flask.redirect('/6')

@app.route('/<max>')
def simple_roll(max):
    return flask.redirect('/roll/{max}/{random}'.format(max=max, random = id_generator()))

@app.route('/roll/<max>/<id>')
def roll(max, id):
    number = random.randint(1, int(max))
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dice</title>
        <meta charset="utf-8">
        <meta name="description" content="{number}"/>
    </head>
    <body>
        <h1>{number}</h1>
        <p style="display: none">{id}</p>
    </body>
    </html>
    """.format(number = str(number), id = id)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

