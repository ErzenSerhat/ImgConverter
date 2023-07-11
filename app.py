from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Home Page
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    file = request.files['file']
    target_extension = request.form['extension']

    temp_file = 'temp' + os.path.splitext(file.filename)[1]
    file.save(temp_file)

    converted_file = 'converted' + target_extension
    os.rename(temp_file, converted_file)
    return render_template('result.html', converted_file=converted_file)

if __name__ == '__main__':
    app.run()