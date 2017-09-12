import os
import json
import pickle

from flask import Flask, render_template, jsonify


app = Flask(__name__)
app.secret_key = 's0mth1ng s3cr3t'


##### Preparing the Classifier
rf = pickle.load(open(os.path.join(cur_dir, 'ml_model', 'classifier.pkl'), 'rb'))

def classify(event):
    return int(rf.predict([event]))

@app.route('/')
def home():
    return render_template('home.html')


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
