from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

@app.route('/')
def index():
   archivos = os.listdir("static")
   lista = []
   for a in archivos:
       if a.split(".")[1] in ["jpg", "png", "jpeg"]:
           lista.append(a)

   return render_template('index.html', msg = "file loaded successfully", rows = lista)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['POST'])
def uploader_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.root_path, 'static', secure_filename(f.filename)))

      archivos = os.listdir("static")
      lista = []
      for a in archivos:
          if a.split(".")[1] in ["jpg", "png", "jpeg"]:
              lista.append(a)

      return render_template('index.html', msg = "file loaded successfully", rows = lista)

if __name__ == '__main__':
   app.run(debug = True)
