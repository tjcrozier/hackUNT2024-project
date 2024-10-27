from flask import Flask, render_template, request, Response, make_response
import ai_api_requests

app = Flask(__name__)

#url_for('static', filename='design.css')

@app.route("/")
def main():
    return render_template("test.html")

@app.post('/submit')
def process_data():
    print(request.get_data(as_text=True).split(","))
    return make_response("foo")
    
if __name__ == '__main__':
    app.run()