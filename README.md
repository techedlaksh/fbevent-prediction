## Facebook Event Analysis and Interested Count Predictor

This is a project for analysis of Facebook Events and for getting interested count prediction.A Random Forest model was used for training on a large dataset of ~1000 events.Feature engineering,Data cleaning, Data selection and many other techniques were used for this task.

## Tools Used

* Python 2.7
* Pandas
* Sklearn
* NumPy
* Seaborn
* Pickle
* NLTK
* Enchant
## How to run on local machine:

1. **Clone this repo**

      ```sh
      $ git clone https://github.com/techedlaksh/fbevent-prediction
      $ cd fbevent-prediction
      ```
2. **Create new virtual environment**

      ```sh
      $ sudo pip install virtualenv
      $ virtualenv venv
      $ source venv/bin/activate
      $ pip install -r requirements.txt
       ```
3. **Website**

    ```sh
    $ python app.py &
    ```
## Code Details

Below is a brief description for the Code files/folder in repo.

## d3-charts/

This folder contains ipython notebook which were used to clean the data for individual d3-chart & pre-processed data for those charts.

#### DataPre-Processing.ipynb

The script fetches data from MongoDB Client in which data was already saved by another script. The pre-processing of data is done for plotting data on geo-map, generating a word frequency chart and popular categories by different metrics which are showcased using donut chart.

```sh
$ jupyter DataPre-Processing.ipynb
```

## data/
This folder contains ipython notebook which contain implementation for graph api of facebook to extract events data from facebook.

#### DataGraphApi.ipynb
The notebook contains implementation of graph api which is used to to extract ids of ~1000 and store it in ids.json then extract all the data of each event and store it as collection in MongoDB.

**Note** : The raw *data* fetched from graph api resides in `data/precog_db_data`. `data/precog_fb_data/events.bson` has the data and `data/precog_fb_data/events.metadata.json` contains the metadata information about the data.

## model/

This folders contains scripts used for training,tuning model and getting the prediction results.

### Prediction-model.ipynb
This notebook pre-processes all the data to appropriate form which can be used as a training for our prediction model. Random Forest model is also inside this notebook and is used to get the prediction from  the preprocessed data.

```sh
$ jupyter Prediction-model.ipynb
```

**Note** : The trained model with `~98% accuracy` has been exported in this folder as `classifier.pkl` which can be imported anywhere to be used.

## static/ 
This folders contain all the static file such `css, data for charts and donut chart script` to be served in `flask`

## templates/
This folder contains all those html files which is used to be served as frontend of the `flask website` which is hosted on [`fbevent-laksh.herokuapp.com`](//fbevent-laksh.herokuapp.com)



