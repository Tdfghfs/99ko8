from flask import Flask, render_template, request
import sys
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_code():
    code = request.form['code']
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()

    try:
        exec(code)
        result = redirected_output.getvalue()
    except Exception as e:
        result = f"Error: {e}"

    sys.stdout = old_stdout
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
