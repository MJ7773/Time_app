from flask import Flask
app = Flask(__name__)


@app.route('/time')
def get_time():
    date = datetime.now()
    return date.strftime("%H:%M:%S %d/%m/%y")


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
