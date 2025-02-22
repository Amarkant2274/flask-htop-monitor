from flask import Flask
import subprocess
import datetime
import getpass
import pytz
import os

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get username
    username = getpass.getuser()
    
    # Get IST time
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')
    
    # Get top output
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    
    # Your name (replace with your actual name)
    name = "Amarkant"  # Make sure to put your actual name here!
    
    return f"""
    <html>
        <body>
            <pre>
Name: {name}
Username: {username}
Server Time (IST): {server_time}

Top Output:
{top_output}
            </pre>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)