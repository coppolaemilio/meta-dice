from flask import Flask
from random import randint
app = Flask(__name__)

@app.route('/<max>')
def roll(max):
    number = randint(1, max)

    return """
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="description" content="{number}"/>
    </head>
    <body>
    <h1>{number}</h1>
    </body>
    </html>
    """.format(number=number)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

