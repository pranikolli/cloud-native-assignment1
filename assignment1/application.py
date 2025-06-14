from flask import Flask, request
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# Add "greetings" route
# Read "GREETING" environment variable and return its value
@app.route("/greetings")
def greetings():
    greeting = os.getenv("GREETING", "Hello!")
    return greeting


# Add "listcontents" route
# Read contents of "hostfolder" and return the contents
@app.route("/listcontents")
def listcontents():
    hostfolder = os.getenv("HOSTFOLDER", ".")
    try:
        contents = os.listdir(hostfolder)
        return "<br>".join(contents)
    except Exception as e:
        return "Error description: "+ str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001) # Change port to 5001
