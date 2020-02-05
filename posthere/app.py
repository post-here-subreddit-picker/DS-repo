from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
import pickle



def create_app():
    app = Flask(__name__)
    model = pickle.load(open('posthere/Model.pkl', 'rb'))
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
            prediction = model.predict([inputs])[0]
            message = 'You want to post this here! {}'.format(prediction)
            return render_template('base.html', message=message, prediction=prediction)


    
    return app


