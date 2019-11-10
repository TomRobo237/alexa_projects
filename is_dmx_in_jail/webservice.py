from flask import Flask
from flask_ask import Ask, statement
from src.dmx_in_jail_status import dmx_status

app = Flask(__name__)
ask = Ask(app, '/')


@ask.launch
def start_skill():
    return statement(dmx_status()[0])


if __name__ in "__main__":
    app.run(debug=True)