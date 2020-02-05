from flask import Flask, render_template, request
import pickle



def create_app():
    app = Flask(__name__)
    model = pickle.load(open('posthere/model2.pkl', 'rb'))
   

    @app.route('/')
    def hello():
        return render_template('home.html', title='Home')

    @app.route('/model', methods=['POST'])
    @app.route('/model/<title>', methods=['GET'])
    def prediction(title=None):
        try:
            if request.method == 'POST':
                title = request.values['title']
        except KeyError:
            return ('''Bad request: one of the required values 
            was missing in the request.''')
        else:
            prediction = model.predict([title])[0]
            return str(prediction)

    
    return app


