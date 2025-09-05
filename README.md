# Company Website Backend (Flask)

This project is a backend implementation for a mobile UI of the Genrobotics website, built using Flask and SQLite. It supports 8 service pages, each with a form and submit button that stores user input in a database.

## 🔧 Tech Stack
- Python 3
- Flask
- SQLite
- DB Browser for SQLite
- HTML (Jinja templates)
- GitHub + GitHub Desktop
- Render (Cloud Hosting)

## 🚀 Features
- Dynamic routing for 8 service pages
- Form submission with POST requests
- Data persistence in `submissions.db`
- Verified using DB Browser

## 📂 Folder Structure
flask_app/ 
   ├── app.py
   ├── requirements.txt 
   ├── README.md 
   ├── templates/ 
         └── form_template.html
   ├── instance/ 
         └── submissions.db



## 🛠️ Setup Instructions

1. Clone the repo or download the folder
2. Create and activate virtual environment:
       python -m venv venv
       .\venv\Scripts\Activate.ps1  
3. Fix PowerShell script execution policy (only if activation fails).
      Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
      (after running this , run the activation command above.)
4. Install project dependencies
      pip install -r requirements.txt
5. Run the flask app
      python app.py
6. Visit the backend in the browser
      http://127.0.0.1:5000/web-design
      http://127.0.0.1:5000/seo
      http://127.0.0.1:5000/app-development
      http://127.0.0.1:5000/branding
      http://127.0.0.1:5000/content-writing
      http://127.0.0.1:5000/digital-marketing
      http://127.0.0.1:5000/ecommerce
      http://127.0.0.1:5000/ui-ux
7  Verify submissions Open submissions.db in DB Browser for SQLite to inspect stored form data.
   
## 🌐 Hosted Link
Live backend: https://genrobotics-backend.onrender.com

## 🚀 Available Routes
- `/Bandicoot`
- `/Bandicoot-Mobility`
- `/G-Mammoth`
- `/Wilboar`
- `/G-Crow`
- `/Sanitation-Infrastructure`
- `/Confined-space-saftey`
- `/Solution-for-unique-challenges`


 
     

         
