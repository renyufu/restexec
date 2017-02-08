import cmd
import os
import subprocess
import sys
import tempfile

import flask

app = flask.Flask('restexec')


""" static file serv """
@app.route('/build/<path:path>')
def send_file(path):
    apikey = flask.request.headers.get('X-Auth-Token')
    if apikey != os.environ.get('TOKEN'):
        return "Check your auth TOKEN", 401
    return flask.send_from_directory('build', path)


""" RESTful command executor """
@app.route('/execute', methods=['POST'])
def execute():
    apikey = flask.request.headers.get('X-Auth-Token')
    if apikey != os.environ.get('TOKEN'):
        return "Check your auth TOKEN", 401

    command = flask.request.json.get('command')

    if not command:
        return 400

    """ Check command """
    if not command in os.environ.get('CMDS').split(','):
        return "command '" + command + "' not supported.", 401

    with tempfile.TemporaryFile() as stdout:
        status = subprocess.call(command,
                                 shell=True,
                                 stdout=stdout,
                                 stderr=subprocess.STDOUT)
        stdout.seek(0)
        output = stdout.read()

    response = {
        'status': status,
        'output': output,
    }

    return flask.jsonify(response)


def run(location):
    # Grab the port to start the server on
    (_, port) = location.split(':')

    if not os.environ.get('TOKEN'):
        print "WARNING! No TOKEN specified, running without authentication"

    if not os.environ.get('CMDS'):
        print "WARNING! No CMDS specified, can't execute any command"

    app.run('0.0.0.0', port=int(port), debug=True, ssl_context='adhoc')
    """app.run('0.0.0.0', port=int(port), debug=True)"""


def main():
    run("0.0.0.0:80")


if __name__ == '__main__':
    main()
