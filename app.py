from flask import Flask,render_template
import requests
from requests.exceptions import RequestException

app = Flask(__name__)

@app.route("/")
def home():
    try:
        response = requests.get("https://api.github.com/users/Devadathan-dev/repos")
        data = response.json()
    except RequestException:
        return render_template("index.html", projects=[],error="Unable to load projects right now. Please view them directly on GitHub.", github_url="https://github.com/Devadathan-dev?tab=repositories")
    if not isinstance(data, list):
        return render_template("index.html", projects=[],error="Unable to load projects right now. Please view them directly on GitHub.", github_url="https://github.com/Devadathan-dev?tab=repositories")
    projects =[]            
    for repo in data:
        projects.append({
            "title": repo["name"],
            "description": repo["description"] or "No description provided.",
            "link": repo["html_url"],
            "updated_at": repo["updated_at"]
        })
    projects = sorted(projects, key=lambda repo: repo["updated_at"], reverse=True)
    return render_template("index.html", projects=projects[:3])


if __name__ == "__main__":
    app.run(debug=True)
    
