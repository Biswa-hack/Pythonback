from flask import Flask, send_file
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('run_script.html')

@app.route('/run-merger')
def run_merger():
    try:
        result = subprocess.run(['python', 'merger.py'], capture_output=True, text=True, check=True)
        return "Script executed successfully.\n" + result.stdout
    except subprocess.CalledProcessError as e:
        return f"Script error:\n{e.stderr}"

if __name__ == '__main__':
    app.run(debug=True)
