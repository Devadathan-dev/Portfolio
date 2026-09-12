# Portfolio

A personal portfolio website built with Flask, showcasing my projects, skills, and background as a Python and Salesforce developer.

## 🛠️ Tech Stack
- **Backend:** Python, Flask
- **Templating:** Jinja2
- **Frontend:** HTML5, CSS3
- **External API:** GitHub REST API

## ✨ Features
- Live project listing fetched dynamically from the GitHub API — automatically shows my 3 most recently updated repositories, no manual updates needed
- Graceful fallback to a direct GitHub profile link if the API is unavailable or rate-limited
- Responsive, single-page layout with anchor navigation (About / Projects / Contact)
- Downloadable resume
- Links to GitHub, LinkedIn, and email contact

## 📂 Project Structure

├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│ └── index.html
└── static/
├── style.css
└── Devadathan_Namboothiri_Resume.pdf

## 🚀 Running Locally

1. Clone the repository
```bash
   git clone https://github.com/Devadathan-dev/Portfolio.git
   cd Portfolio
```

2. Install dependencies
```bash
   pip install -r requirements.txt
```

3. Run the app
```bash
   python app.py
```

4. Open `http://127.0.0.1:5000` in your browser

## 📫 Contact
- Email: devadathannamboothirip1@gmail.com
- GitHub: [github.com/Devadathan-dev](https://github.com/Devadathan-dev)
- LinkedIn: [linkedin.com/in/dn2002](https://www.linkedin.com/in/dn2002/)