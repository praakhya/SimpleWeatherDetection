from flask import Flask, render_template
import csv
app = Flask(__name__)


@app.route("/")
def getWeatherData():
    data=[]
    with open('data.txt', newline='') as csvfile:
        spamreader = csv.DictReader(csvfile, 
                                    ["Time",
                                     "PM2.5",
                                     "PM10",
                                     "Pressure",
                                     "Temperature",
                                     "Humidity"], delimiter=',')
        try:
            for row in spamreader:
                data.append(row)
        except:
            pass
        print(data)
        heading=["Time","PM2.5","PM10","Pressure","Temperature","Humidity"]
        
        return render_template('pageTemplate.jinja', readings=data, headings = heading)
