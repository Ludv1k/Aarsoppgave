from flask import Flask, render_template
import re

# Create the Flask app
app = Flask(__name__)

# Create route
@app.route('/')
def root():
    return render_template('base.html')

@app.route('/hi')
def actually_just_testing():
    return render_template('test2.html')

# Run the Flask app
if __name__ == '__main__':
    # Set the app to be accessible on the network
    app.run(host='0.0.0.0', port=8080, debug=True)