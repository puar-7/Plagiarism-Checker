from flask import Flask, request, render_template
from combined_checker import combined_plagiarism_checker

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_plagiarism():
    code1 = request.form['code1']
    code2 = request.form['code2']
    
    # Run plagiarism checker
    is_plagiarized = combined_plagiarism_checker(code1, code2)
    
    # Return result to frontend
    if is_plagiarized:
        return render_template('index.html', result="Plagiarism Detected")
    else:
        return render_template('index.html', result="No Plagiarism Detected")

if __name__ == '__main__':
    app.run(debug=True)
