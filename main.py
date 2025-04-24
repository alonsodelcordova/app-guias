from app import create_app
from config import config
from decouple import config as config_decouple
from flask import render_template

enviroment = config['development']

if config_decouple('PRODUCTION', default=False) == 'True':
    enviroment = config['production']


app = create_app(enviroment)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
