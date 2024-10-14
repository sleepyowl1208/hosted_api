from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    # Return a JSON response
    return jsonify({
        "message": "Welcome to Python World"
    })

# Define the route for "/greetings"


@app.route('/greetings')
def greetings():
    # Return a JSON response
    return jsonify({
        "message": "Greetings from Python"
    })


# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
