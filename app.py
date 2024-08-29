from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def Index():
    return render_template("index.html")

@app.route("/Summarize", methods=["GET", "POST"])
def Summarize():
    if request.method == "POST":  
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": "Bearer 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"}
        
        data = request.form.get("data", "")  
        minL = maxL//4
        maxL = int(request.form["maxL"])
        
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
        
        output = query({
            "inputs": data,
            "parameters": {"min_length": minL, "max_length": maxL},
        })[0]
        return render_template("index.html", result=output["summary_text"])
    else:
        return render_template("index.html")
    
if __name__ == '__main__':
    app.run(debug=True)




'''from flask import Flask, render_template, url_for, request
import requests


app = Flask(__name__)
@app.route("/", methods = ["GET","POST"])
def Index():
    return render_template("index.html")

@app.route("/Summarize", methods =["GET", "POST"])
def Summarize():
    if request.methods == "POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": "Bearer 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"}
        
        data = request.form["data"]
        minL = 20
        maxL = 70
        
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)   
            return response.json()
        
        output = query({
             "inputs": data,
             "parameters":{"min_length":  minL,"max_length": maxL},
        }) 
        return render_template("index.html",result = output)
    else:
        return render_template("index.html")
    
if __name__ == '__main__':
    app.debug=True
    app.run()'''