from flask import Flask #From flask module importing Flask class
from flask import render_template #to run the file

app = Flask(__name__) #ap = instance of Flask; __name__=inbuilt name

#to insert dynamic data in html file

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location" : "Bengaluru, India",
        "salary" : "Rs. 10,00,000"
    },
    {
        "id": 2,
        "title": "Data Enginer",
        "location" : "Bengaluru, India",
        "salary" : "Rs. 20,00,000"
    },
    {
        "id": 3,
        "title": "Front end",
        "location" : "Chennai, India",
        "salary" : "Rs. 10,00,000"
    },
    {
        "id": 4,
        "title": "Backend engineer",
        "location" : "Bengaluru, India",
        "salary" : "Rs. 60,00,000"
    },
]

@app.route("/") #Routing this to home page (/ = homepage)
def Hello():
    #return "Hello world"
    return render_template("home.html",jobs = JOBS)#providing dynamic data as arguement.




#in order to run the above stuffs:
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)

#changes in github = version control tab; commit and push
#templates folder = html files
#static = Explicit file upload