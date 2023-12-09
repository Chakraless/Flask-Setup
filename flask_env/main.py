from flask import Flask, request, render_template


app = Flask(__name__, static_url_path='/static')



@app.route("/home")
def home():
    return render_template('index.html')
@app.route("/test")
def test():
    return "<h1>TESTING<h1>"

@app.route("/socials")
def socials():
    return render_template('socials.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')


if __name__ == '__main__':
    app.run(debug=True)