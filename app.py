from flask import Flask, request, render_template
import yaml
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        # ⚠️ YAML deserialization vulnerability (PyYAML unsafe load)
        data = request.form["yaml_input"]
        try:
            parsed = yaml.load(data)  # vulnerable
            result = f"Parsed YAML: {parsed}"
        except Exception as e:
            result = f"Error: {e}"

    return render_template("index.html", result=result)

@app.route("/request")
def request_data():
    url = request.args.get("url", "")
    # ⚠️ SSRF vulnerability: no validation on URL
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        return f"Request failed: {e}"

if __name__ == "__main__":
    app.run(debug=True)
