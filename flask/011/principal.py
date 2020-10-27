from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      lista = [x.split(',') for x in open(f.filename).readlines()]
      print(len(lista))
      return render_template('showall.html', msg = "file loaded successfully", rows = lista)

if __name__ == '__main__':
   app.run(debug = True)
