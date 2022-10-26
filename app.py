from flask import Flask, send_from_directory, redirect, request, url_for, render_template

app = Flask(__name__, static_url_path='', static_folder='ui/build/')

# TODO: after adding login methods add login verification to each page

@app.route('/')
def index():
    # if auth-login
    return redirect('/projects')
    # else go to login page

@app.route('/projects')
def projects_page():
    return send_from_directory('ui/build/', 'index.html')

@app.route('/projects/checkIn/<projectid>/<int:qty>')
def checkOut_hardware(projectid, qty):
    message = str(qty) + " hardware units checked in from project: " + projectid
    return {"message": message}


@app.route('/projects/checkOut/<projectid>/<int:qty>')
def checkIn_hardware(projectid, qty):
    message = str(qty) + " hardware units checked out from project: " + projectid
    return {"message": message}


@app.route('/projects/join/<projectid>')
def joinProject(projectid):
    message = "joined project: " + projectid
    return {"message": message}


@app.route('/projects/leave/<projectid>')
def leaveProject(projectid):
    message = "left project: " + projectid
    return {"message": message}

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))