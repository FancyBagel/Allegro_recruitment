# Allegro_recruitment
My entry for Task 3 of Allegro Summer Experience Software Engineer Intern recruitment process.
## Technologies
* Python version 3.8.5
* Flask version 1.1.2
* Waitress version 2.0.0
## Installation
After downloading the repo, install required packages by running the following command in project's main folder:
```
$ pip3 install -r requirements.txt
```
## Setup
To run the app from the interface and port of your choice, run
```
$ python3 app.py [HOST] [PORT]
```
For example, to listen on every available network interface and port 5000, run
```
$ python3 app.py 0.0.0.0 5000
```
## Usage
To get the desired information about a GitHub user's repo list and repos' stargazer counts, simply send a GET request:
```
GET [SERVER_ADDRESS]:[PORT]/repo-list?username=<desired-user-name>
```
In exchange, the app will send a JSON file with all desired information.
For example, a request
```
GET [SERVER_ADDRESS]:[PORT]/repo-list?username=FancyBagel
```
will receive a response:
```
{
    "repo_list": [
        {
            "name": "Allegro_recruitment",
            "stargazers_count": 0
        },
        {
            "name": "DS4Windows",
            "stargazers_count": 0
        },
        {
            "name": "pointless-stuff",
            "stargazers_count": 0
        },
        {
            "name": "QuiteWarm",
            "stargazers_count": 0
        }
    ],
    "total_stargazers": 0
}
```
## Possible expansion
The app has much potential for expansion, including but not limited to further information about user's public repos and about users themselves.
