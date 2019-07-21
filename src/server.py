import os
import logging

from utils import get_normalized_day
from podcast import get_last_podcast, get_podcast, get_available_days

from flask import Flask, json, render_template
from flask_ask import Ask, request, session, question, statement, audio
from flask_ask import current_stream, logger

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)


@ask.launch
def launch():
    return play_last()

@ask.intent('PlayLastIntent')
def play_last():
    last_podcast_text = render_template('last_podcast')
    return audio(last_podcast_text).play(get_last_podcast())

@ask.intent('PlayDayIntent',
    mapping={'day': 'Day'})
def play_day(day):
    normalized_day = get_normalized_day(day)
    if normalized_day not in get_available_days():
        return supported_days()
    day_podcast = render_template('day_podcast', day=normalized_day)
    return audio(day_podcast).play(get_podcast(normalized_day))

@ask.intent('SupportedDaysIntent')
def supported_days():
    days = ", ".join(AVAILABLE_DAYS)
    list_days_text = render_template('list_days')
    list_days_reprompt_text = render_template('list_days_reprompt')
    return question(list_days_text).reprompt(list_days_reprompt_text)

@ask.intent('AMAZON.HelpIntent')
def help():
    help_text = render_template('help')
    list_days_reprompt_text = render_template('list_days_reprompt')
    return question(help_text).reprompt(list_days_reprompt_text)

@ask.intent('AMAZON.PauseIntent')
def pause():
    return audio('').stop()

@ask.intent('AMAZON.ResumeIntent')
def resume():
    return audio('').resume()

@ask.intent('AMAZON.StopIntent')
def stop():
    return audio('').clear_queue(stop=True)


if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
