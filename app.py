from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>🚀 Welcome to Jenkins CI/CD</h1>
    <h2>Hello Esha 👋</h2>
    <p>Version 2.0</p>
    <p>Application updated successfully.</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

