from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
        data = [
                ("01-01-2020", 1597)




        
        
        
        
        ]


labels = [row[0]] for row in data]
values = [row[1]] for row in data]
#Alternativ sätt
labels = []
values = []
for row in data:
    labels.append(row[0])
    values.append(row[1])
#return data
return render_template("graph.html"), labels=labels, values=values


if __name__ == "__main__":
    app.run(port=8000, debug=true)
