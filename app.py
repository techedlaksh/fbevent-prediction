import os
import json
import pickle
import facebook

from flask import Flask, render_template, jsonify, request, redirect
from wtforms import Form, TextAreaField, validators



app = Flask(__name__)
app.secret_key = 's0mth1ng s3cr3t'


##### Preparing the Classifier
cur_dir = os.path.dirname(__file__)
rf = pickle.load(open(os.path.join(cur_dir, 'ml_model', 'classifier.pkl'), 'rb'))

token = 'EAAD4wuQJXMQBAOeLbGArkUVA5rlu3VndjMmyBqlc33vTbXAl9uZB4fQqZCj1ByAAjqvHq1vfLx8MZBZAOc3Ll9kaRZAUZATXcDZB2bR2PsZALxfZCfKzvZC1XhBI4gCM2JWI6C5v9uc24mJByxteLGZBUzU7G9HFFYn1VtqCo9BXDz6cgZDZD'



class EventForm(Form):
    eventid = TextAreaField('', [validators.DataRequired(), validators.length(min=5)])

def classify(eventid):
    graph = facebook.GraphAPI(access_token=token, version = '2.10')
    field_events = 'attending_count, can_guests_invite, guest_list_enabled, maybe_count, noreply_count, interested_count'
    temp_event = graph.get_object(id=eventid, fields=field_events)
    order_list = ['attending_count', 'can_guests_invite', 'guest_list_enabled', 'maybe_count', 'noreply_count']
    event = [temp_event[x] for x in order_list]
    print event
    return int(rf.predict([event])), int(temp_event['interested_count'])

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/event')
def event():
    try:
        form = EventForm(request.form)
        return render_template('eventform.html', form=form)
    except:
        return "Seems like developer has not updated the site yet! Contact => <a href='//github.com/techedlaksh'> Laksh"

@app.route('/results', methods =['POST'])
def results():
    form = EventForm(request.form)
    if request.method == 'POST' and form.validate():
        eventid = request.form['eventid']
        prediction, truth = classify(eventid)
        return render_template('results.html', prediction = prediction, truth = truth)
        # prediction = request.form['name']
    # field = request.form['name']
        # return 'Interested Count is: %s' % prediction
    # print prediction
    try:
        pass
        # return render_template('results.html')
    except:
        return "Seems like developer has not updated the site yet! Contact => <a href='//github.com/techedlaksh'> Laksh"


@app.route('/geoplot')
def geoplot():
    try:
        return render_template('geoplot.html')
    except:
        return "Seems like developer has not updated the site yet! Contact => <a href='//github.com/techedlaksh'> Laksh"

@app.route('/popcat')
def popcat():
    try:
        return render_template('popcat.html')
    except:
        return "Seems like developer has not updated the site yet! Contact => <a href='//github.com/techedlaksh'> Laksh"


@app.route('/wordcloud')
def wordcloud():
    try:
        return render_template('wordcloud.html')
    except:
        return "Seems like developer has not updated the site yet! Contact => <a href='//github.com/techedlaksh'> Laksh"


@app.route('/posneg')
def posneg():
    try:
        return render_template('posneg.html')
    except:
        return "Seems like developer has not updated the site yet! Contact => <a href='//github.com/techedlaksh'> Laksh"


@app.route('/get/<file>')
def get(file):
    if file in ['word_freq']:
        with open('static/data/'+file+'.json') as f:
            data = json.load(f)
        return jsonify(data)
    else:
        return 'File not Found !'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)
