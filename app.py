from flask import Flask, request, render_template_string
import yaml
import requests
from utils import unsafe_deserialize

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the vulnerable app!"

@app.route('/ssrf')
def ssrf():
    url = request.args.get('url')
    if not url:
        return "Please pass a URL param"
    r = requests.get(url)
    return f"Response from {url}: {r.text[:200]}"

@app.route('/yaml', methods=['POST'])
def unsafe_yaml():
    data = request.data.decode()
    parsed = yaml.load(data)  # unsafe
    return f"Parsed YAML: {parsed}"

@app.route('/template')
def ssti():
    user_input = request.args.get("q", "")
    return render_template_string(user_input)

@app.route('/deserialize', methods=['POST'])
def deserialize():
    data = request.data.decode()
    return unsafe_deserialize(data)

if __name__ == '__main__':
    app.run(debug=True)
