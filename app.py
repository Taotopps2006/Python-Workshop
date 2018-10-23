from flask import Flask, render_template

app = Flask(__name__)

person = "Insert Name Here"


@app.route('/')
def test():
    return render_template('index.html', name=person)


if __name__ == '__main__':
    app.run()
