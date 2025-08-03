from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ السيرفر شغّال'

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json.get('code', '')
    try:
        result = subprocess.check_output(['python3', '-c', code], stderr=subprocess.STDOUT, timeout=5)
        return jsonify({'output': result.decode()})
    except subprocess.CalledProcessError as e:
        return jsonify({'output': e.output.decode()})
    except Exception as e:
        return jsonify({'output': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
