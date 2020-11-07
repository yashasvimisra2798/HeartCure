#inporting relevant libraries
import numpy as np
import pickle
from flask import Flask, request, render_template
import numpy.random._pickle

app = Flask(__name__,template_folder='templates/')
model = pickle.load(open('model(gb).pkl','rb'))

@app.route('/')
def heart():
    return render_template('outline.html')


@app.route('/predict',methods=['GET','POST'])
def predict():
    
    if request.method == "GET":
        return render_template('Heart.html')
    features = [float(i) for i in request.form.values()]
    array_features = [np.array(features)]
    prediction = model.predict(array_features)
    output = prediction

    if output == 1:
        return render_template('Heart.html', result = 'The patient is not likely to have heart disease!')
    else:
        return render_template('Heart.html',result='The patient is likely to have heart disease!')


if __name__ == '__main__':
    app.run(debug=True)