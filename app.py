from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# from forms import SignUpForm



def create_app():
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rpg_db.sqlite3'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

    # db = SQLAlchemy(app)


    @app.route('/')
    def hello():
        return render_template('home.html', title='Home')


    @app.route('/model', methods=["POST", "GET"])
        # def search():
        # title = request.values['title']
        # self_text = request.values['selftext']
        # prediction = predict(title, self_text)
        #     message = 'You want to post this here! {}'.format(prediction)
    def model():
        return "Hello world."

    
    return app


