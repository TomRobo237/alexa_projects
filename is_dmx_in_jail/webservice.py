from flask import Flask
from flask_ask import Ask, statement
from src.dmx_in_jail_status import dmx_status

app = Flask(__name__)
ask = Ask(app, '/alexa/dmx')


@ask.launch
def start_skill():
    message, jailbool = dmx_status()
    status = "Free as a bird!" if jailbool is False else 'In the clink.'
    return statement(message).simple_card("DMX Incarceration status:", status)

@ask.intent('Any')
def any_intent():
    return start_skill()


if __name__ in "__main__":
    app.run(debug=True, host='0.0.0.0')