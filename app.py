from flask import Flask, render_template, request
import json

app = Flask(__name__)
filename = '25042020.json'

@app.route('/', methods=['GET'])
def index():
    return(render_template('index.html'))

@app.route('/', methods=['POST'])
def result():
    #GET REQUEST DATA FROM THE FRONTEND
    country1 = request.form['country']
    country2 = request.form['country2']
    country3 = request.form['country3']

    #GET CASES FOR COUNTRIES
    casesCountry1 = getCases(country1)
    casesCountry2 = getCases(country2)
    casesCountry3 = getCases(country3)

    #GET DEATHS FOR COUNTRIES
    deathsCountry1 = getDeaths(country1)
    deathsCountry2 = getDeaths(country2)
    deathsCountry3 = getDeaths(country3)

    #GET DATES
    dateLabels = getDates()

    print(deathsCountry2)
    print(dateLabels)
    return(render_template('index.html', country1=country1, country2=country2, country3=country3, casesCountry1=casesCountry1, casesCountry2=casesCountry2, casesCountry3=casesCountry3, deathsCountry1=deathsCountry1, deathsCountry2=deathsCountry2, deathsCountry3=deathsCountry3, dateLabels=dateLabels  ))

def getCases(country):
    with open(filename) as json_file:
        jsonData = json.load(json_file)
        caseList = []
        for record in jsonData['records']:
            if record['countryterritoryCode'] == country:
                caseList.append(int(record['cases']))
    return(list(reversed(caseList)))

def getDates():
    with open(filename) as json_file:
        jsonData = json.load(json_file)
        dateList = []
        for record in jsonData['records']:
            if record['countryterritoryCode'] == 'DEU':
                dateList.append(record['dateRep'])
    return(list(reversed(dateList)))

def getDeaths(country):
    with open(filename) as json_file:
        jsonData = json.load(json_file)
        deathList = []
        for record in jsonData['records']:
            if record['countryterritoryCode'] == country:
                deathList.append(int(record['deaths']))
    return(list(reversed(deathList)))


if __name__ == '__main__':
    app.run(debug=True)
