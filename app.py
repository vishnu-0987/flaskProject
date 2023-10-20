import requests
from flask import Flask, render_template, request

app = Flask(__name__)

def FindPresence(username):
    # Define the websites to check
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    websites = {
        'LinkedIn': 'https://www.linkedin.com/in/',
        'Facebook': 'https://www.facebook.com/',
        'Twitter': 'https://twitter.com/',
        'Instagram': 'https://www.instagram.com/',
        # Add more websites here
    }

    results = {}
    for site, url in websites.items():
        link = url + username
        response = requests.get(link, headers)

        if response.status_code == 200:
            results[site] = "User name already exists"
        else:
            results[site] = "Available"

    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None

    if request.method == 'POST':
        username = request.form['username']
        results = FindPresence(username)

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
