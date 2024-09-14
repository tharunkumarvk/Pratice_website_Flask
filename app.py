from flask import Flask #From flask module importing Flask class
from flask import render_template #to run the file

app = Flask(__name__) #ap = instance of Flask; __name__=inbuilt name

@app.route("/") #Routing this to home page (/ = homepage)
def Hello():
    #return "Hello world"
    return render_template("home.html")

#in order to run the above stuffs:
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)

#changes in github = version control tab; commit and push
#templates folder = html files