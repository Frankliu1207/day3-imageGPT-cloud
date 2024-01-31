from flask import Flask,request,render_template
import json
import time
import requests

headers={
    "Authorization" : "Token r8_9yQxZtX50iMqi6nyxS6YdIzMnXouLxS2PVwCf",
    "Content-Type" : "application/json"
}

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        q = request.form.get("q")
        data = json.dumps(
            {
                "version" : "db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",    
                "input" : {"prompt":q}
            }
        )
        r = requests.post('https://api.replicate.com/v1/predictions',data=data,headers=headers)
        time.sleep(15)
        r = r.json()["urls"]["get"]
        r = requests.post(r,headers=headers).json()["output"]
        return(render_template("index.html.html",r=r[0]))
    else:
        return(render_template("index.html.html",r="Waiting for your entry"))

if __name__ == "__main__":
    app.run()
