from flask import Flask, render_template, request
import pickle
import re
app = Flask(__name__)

vector=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('phishing.pkl','rb'))

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        url=request.form['url']
        cleaned_url = re.sub(r"https?://(www\.)?", "", url)
        # print(url)
        predict=model.predict(vector.transform([cleaned_url])[0])
        # print(predict)
        if predict == 'bad':
            predict = "The website is likely a phishing attempt."
        elif predict == 'good':
            predict = "The website is likely safe."
        else :
            predict = "Unable to determine the safety of the website."  

        return render_template("index.html", predict=predict)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)