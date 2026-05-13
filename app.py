from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Thorpe Park ID is 2
    api_url = "https://queue-times.com/parks/2/queue_times.json"
    
    try:
        response = requests.get(api_url)
        # Raises an error if the website is down
        response.raise_for_status() 
        data = response.json()
        all_lands = data.get('lands', [])
    except Exception as e:
        print(f"Error: {e}")
        all_lands = []

    return render_template('index.html', lands=all_lands)

if __name__ == '__main__':
    app.run(debug=True)