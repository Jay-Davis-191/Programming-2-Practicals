from flask import Flask, redirect
app = Flask(__name__)

name = input("Name: ")
celsius = float(input("Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

@app.route('/')
def hello():
    return redirect("/greet", code=302)


@app.route('/greet')
def greetings():
    return "Hello World :)"


def redirection():
    return redirect("/greet/{}".format(name, code=302))


@app.route('/greet/{}'.format(name))
def greet():
    return "Hello {}".format(name)


@app.route('/f/{}'.format(celsius))
def convert():
    return redirect("/f/{}".format(fahrenheit))


@app.route('/f/{}'.format(fahrenheit))
def celsius(fahrenheit):
    return fahrenheit


if __name__ == '__main__':
    app.run()
