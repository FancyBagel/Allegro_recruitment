from flask import Flask, request, jsonify
import requests
import json
from sys import argv

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello there"

@app.route("/repo-list", methods=['GET'])
def form_example():
    username = request.args.get('username')
    print("WHAT")
    print(username)

    page_iter = 1
    star_sum = 0
    repos_count = 0

    list = []

    while True:
        github_url = 'https://api.github.com/users/{}/repos?page={}'.format(username, page_iter)
        print(github_url)
        page_iter += 1
        resp = requests.get(github_url)
        data = json.loads(resp.text)
        print(data)
        if 'message' in data:
            if data['message'] == 'Not Found':
                return jsonify(message="User not found")
            return jsonify(message="GitHub API malfunction occured")
        ##print(data['message'])
        for i in range(len(data)):
            ##print(data[i]['name'] + " " + str(data[i]['stargazers_count']))
            star_sum += data[i]['stargazers_count']
            info = {}
            info['name'] = data[i]['name']
            info['stargazers_count'] = data[i]['stargazers_count']
            list.append(info)
        repos_count += len(data)
        if len(data) < 30:
            break

    return jsonify(total_stargazers=star_sum, repo_list=list)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host=argv[1], port=argv[2])