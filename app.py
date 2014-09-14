import os, re
import subprocess
from flask import Flask, render_template, request
from lxml import html
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/jqchx', methods=['POST'])
def jqchx():
    #incoming form data:
    url = request.form['url']

    #check empty (js off on the original form?)
    if not url:
        return "Error: please submit a url"

    regex = re.compile(
    r'^(?:http)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    # check some validity:
    validurl = re.match(regex, url)
    if not validurl:
        return "Error: please submit a valid url"

    # so it's reasonably well-formed, let's access the page:
    process = subprocess.Popen(['static/js/vendor/phantomjs', 'static/js/vendor/jqchx.js', url], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = process.wait()

    success = ''
    error = ''

    # Read from pipes
    for line in process.stdout:
        success += line.rstrip()
    for line in process.stderr:
        errors += line.rstrip()

    # sanity checking:
    #print success

    #check stderr 1st for any system/network errors:

    # if we're ok, check the stdout for any passed error message:
    # a little regex to find if there's an error, or a reference error:
    # test more to find any edge cases
    matchobj = re.search(r'error', success, re.M|re.I)

    if(matchobj):
        return "jQuery is not used at this site"
    else:
        return 'jQuery Version ' + success

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5005.
    port = int(os.environ.get('PORT', 5005))
    app.run(host='0.0.0.0', port=port, debug=True)
