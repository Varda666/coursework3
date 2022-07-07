from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def http_500_handler():
    return ("<h2>500 Error</h2>", 500)

app.run()