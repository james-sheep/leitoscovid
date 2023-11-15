from flask import Flask, render_template, request
import os
from flask import Flask
from consulta import busca_api

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
  
    if  request.method == 'POST':
        municipio = request.form['cidade']
        contexto = busca_api(municipio)
        return render_template('index.html', context=contexto)
    
    else:
    
        return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    