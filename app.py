import os
import json
import pickle

from flask import Flask, render_template, jsonify, request, redirect
from wtforms import Form, TextAreaField, validators



app = Flask(__name__)
app.secret_key = 's0mth1ng s3cr3t'


##### Preparing the Classifier
cur_dir = os.path.dirname(__file__)
rf = pickle.load(open(os.path.join(cur_dir, 'ml_model', 'classifier.pkl'), 'rb'))

class EventForm(Form):
    eventid = TextAreaField('',
                                [validators.DataRequired(),
                                validators.length(min=5)])

def classify(event):
    return int(rf.predict([event]))

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
        prediction = request.form['eventid']
        return render_template('results.html', prediction = prediction)
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
