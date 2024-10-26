from flask import Flask, render_template

app = Flask(__name__)

#url_for('static', filename='design.css')

@app.route("/")
def main():
    return render_template("siteface.html")

if __name__ == '__main__':
    app.run()