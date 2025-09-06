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
- https://genrobotics-backend.onrender.com/Bandicoot
- https://genrobotics-backend.onrender.com/Bandicoot-Mobility
- https://genrobotics-backend.onrender.com/G-Mammoth
- https://genrobotics-backend.onrender.com/Wilboar
- https://genrobotics-backend.onrender.com/G-Crow
- https://genrobotics-backend.onrender.com/Sanitation-Infrastructure
- https://genrobotics-backend.onrender.com/Confined-space-saftey
- https://genrobotics-backend.onrender.com/Solution-for-unique-challenges

7.  Verify submissions Open submissions.db in DB Browser for SQLite to inspect stored form data.
   
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


 
     

         

