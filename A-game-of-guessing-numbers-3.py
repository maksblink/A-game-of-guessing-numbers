from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def guess():
    if request.method == 'POST':
        ans = request.form['subject']
        min = int(request.form['min'])
        max = int(request.form['max'])
        if ans == "win":
            return "I win!"
        elif ans == "toobig":
            max = int(request.form['guess'])
        elif ans == "toosmall":
            min = int(request.form['guess'])
        if abs(max - min) <= 1:
            return "Don't cheat on me!"
        return options(min, max)
    else:
        return options()


def options(min=0, max=1000):
    guess = int((max - min) / 2) + min
    return f"""
       Make up a number from 0 to 1000 and I'll guess it in 10 moves max.
       <br>
       I guess: {guess}
    <form action="/" method="POST">
                <input type="hidden" name="min" value="{min}">
                <input type="hidden" name="max" value="{max}">
                <input type="hidden" name="guess" value="{guess}">
            <button name="subject" type="submit" value="win">
                You win
            </button>
            <button name="subject" type="submit" value="toobig">
                Too big
            </button>
            <button name="subject" type="submit" value="toosmall">
                Too small
            </button>
    </form>
    """


if __name__ == '__main__':
    app.run(debug=True)
