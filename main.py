from flask import Flask, render_template, request, Response, make_response
from canopy import asin_to_json

app = Flask(__name__)

#url_for('static', filename='design.css')

@app.route("/")
def main():
    return render_template("test.html")

@app.post('/submit')
def process_data():
    return asin_to_json(request.get_data(as_text=True).split(","))
    
if __name__ == '__main__':
    app.run()