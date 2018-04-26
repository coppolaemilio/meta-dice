from flask import Flask
from random import randint
app = Flask(__name__)

@app.route('/<max>')
def roll(max):
    number = randint(1, int(max))
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

