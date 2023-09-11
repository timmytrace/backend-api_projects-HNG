from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/endpoint', methods=['GET'])
def get_endpoint():
    # Get the query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get the current UTC time and day of the week
    current_utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    current_day = datetime.datetime.utcnow().strftime('%A')

    # Get the GitHub URLs
    github_file_url = request.args.get('github_file_url')
    github_repo_url = request.args.get('github_repo_url')

    # Create the JSON response
    response = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': current_utc_time,
        'track': track,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': 200
    }

    # Return the JSON response with status code 200
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
