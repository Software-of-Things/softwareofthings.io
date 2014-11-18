from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', alt_header=True)


@app.route("/projects/<project_name>")
def project(project_name):
    return render_template('{}.html'.format(project_name))

if __name__ == "__main__":
    app.run(debug=True)
