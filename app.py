import flask
import random
app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.redirect('/6')

@app.route('/<max>')
def roll(max):
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
    </body>
    </html>
    """.format(number=str(number))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

