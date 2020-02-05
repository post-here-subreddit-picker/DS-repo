import pickle


def jayden(inputs):
    model = pickle.load(open('Model.pkl', 'rb'))
    return model.predict([inputs])[0]