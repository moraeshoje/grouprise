from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL (/) that returns 'Hello, World!'
@app.route('/')
def hello_world():
    return 'Hello, World!'

# If this script is executed directly (not imported as a module)
if __name__ == '__main__':
    from waitress import serve  # Import serve function from Waitress
    
    # Serve the Flask application using Waitress on host 0.0.0.0 (all interfaces) and port 80
    serve(app, host='0.0.0.0', port=80)
    
    # Print a message to indicate successful server start on port 80
    print("Server successfully started on port 80.")
