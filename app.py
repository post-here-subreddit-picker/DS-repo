from flask import Flask, render_template, request
from . import predictions
# from flask_sqlalchemy import SQLAlchemy



def create_app():
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rpg_db.sqlite3'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

    # db = SQLAlchemy(app)


    @app.route('/')
    def hello():
        return render_template('home.html', title='Home')


    @app.route('/model')
    def prediction():
        try:
            title = request.args['title']
        except KeyError:
            return ('''Bad request: one of the required values 
            was missing in the request.''')
        else:
            inputs = [str(values) for values in title]
            predict = predictions.jayden(inputs)
            message = 'You want to post this here! {}'.format(prediction)
            return render_template('base.html', message=message, predict=predict)


    
    return app


