# Genrobotics Website Backend (Flask)

This is a modular Flask backend designed to support dynamic service pages, form submissions, and data retrieval for current job openings. Built for interview presentation and real-world integration.


## 🔧 Tech Stack
- Python 3
- Flask
- SQLite
- DB Browser for SQLite
- HTML (Jinja templates)
- GitHub + GitHub Desktop
- Render (Cloud Hosting)

## 🚀 Features
- ✅ A landing page
- ✅ Dynamic routing for 8 service pages
- ✅ HTML form rendering with contextual headings
- ✅ Form submission via POST to `/submit/<page_name>`
- ✅ Data stored in SQLite using SQLAlchemy ORM
- ✅ JSON preview of submitted form data after submission
- ✅ Route to retrieve current job openings from dataset
- ✅ Clean separation of templates and logic for scalability


## 📂 Folder Structure
flask_app/ 
   ├── app.py
   ├── requirements.txt 
   ├── README.md 
   ├── templates/ 
         └── form_template.html
         └── submission_result.html
   ├── instance/ 
         └── submissions.db


## 📄 Service Pages
   Available Routes
- `/Bandicoot`
- `/Bandicoot-Mobility`
- `/G-Mammoth`
- `/Wilboar`
- `/G-Crow`
- `/Sanitation-Infrastructure`
- `/Confined-space-saftey`
- `/Solution-for-unique-challenges`
- `/current-openings`

Each of the routes renders a form with a dynamic heading:
/Bandicoot /Bandicoot-Mobility /G-Mammoth /Wilboar /G-Crow /Sanitation-Infrastructure /Confined-space-saftey /Solution-for-unique-challenges

Each page displays:
> "If you are interested in [page_name]"

Form fields include:
- Full Name
- Email
- Organization
- Message

## 📬 Form Submission

Submitted data is sent to:
POST /submit/<page_name>

Stored in `ContactSubmission` table (`submissions.db`) with fields:
- `page_name`
- `full_name`
- `email`
- `organization`
- `message`

After submission, the user is redirected to a result page showing:


{
  "page": "Bandicoot",
  "status": "success",
  "submitted_data": {
    "full_name": "Najmi",
    "email": "najmi@example.com",
    "organization": "Genrobotics",
    "message": "Excited to collaborate!"
  }
}

📊 Current Openings API
🔹 Route
GET /current-openings


🔹 Description
Connects to the Current_Openings table in submissions.db and returns a list of job openings in JSON format.
🔹 Sample Response
[
  {
    "Job_Title": "Backend Developer",
    "Posting_Date": "2025-09-01",
    "Job_Type": "Full-Time",
    "Job_Des": "Build scalable APIs",
    "Location": "Kerala",
    "Status": "Open"
  },
  {
    "Job_Title": "Data Analyst",
    "Posting_Date": "2025-08-15",
    "Job_Type": "Internship",
    "Job_Des": "Analyze sanitation data",
    "Location": "Remote",
    "Status": "Open"
  }
]



🗂 Project Structure
├── app.py
├── submissions.db
├── templates/
│   ├── form_template.html
│   ├── submission_result.html
│   └── 404.html

🛡️ Error Handling

This backend includes structured error handling to ensure reliability and clarity during runtime. Key areas where error handling is implemented:
- Form Submission (/submit/<page_name>)
Wrapped in a try-except block to catch unexpected input or database errors. If an exception occurs, the API returns a clear JSON response:
{
  "error": "Internal Server Error",
  "details": "Exception message here"
}
- Dynamic Routing (/<page_name>)
Invalid service pages are handled with a custom 404 response using:
return render_template('404.html'), 404
- Database Connection (/current-openings)
Uses error handling to catch SQLite connection issues and malformed queries, returning structured error messages for debugging.


🚀 How to Run Locally

python -m venv venv
venv\Scripts\activate
Fix PowerShell script execution policy (only if activation fails).
      Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
      (after running this , run the activation command above.)
pip install flask flask_sqlalchemy      
Install project dependencies
      pip install -r requirements.txt
Run the flask app
      python app.py

Visit:
http://localhost:5000/Bandicoot
http://localhost:5000/Bandicoot-Mobility
http://localhost:5000/G-Mammoth
http://localhost:5000/G-Crow
http://localhost:5000/Sanitation-Infrastructure
http://localhost:5000/Confined-space-saftey
http://localhost:5000/Solution-for-unique-challenges
http://localhost:5000/current-openings

Verify submissions Open submissions.db in DB Browser for SQLite to inspect stored form data.

🌐 Deployment Instructions

Add Required Files
    Include these two files in the project root:
       - requirements.txt
    List  dependencies:
      flask
      flask_sqlalchemy
Deploying using Render      
Go to https://render.com
-Click “New Web Service”
- Connect your GitHub repository
- Set:
   - Build Command: pip install -r requirements.txt
   - Start Command: python app.py
- Choose a free plan and deploy


## 🌐 Hosted Link
Live backend: https://genrobotics-backend.onrender.com

## If inorder to commit any changes in repository
Do the changes ans save the file 
On terminal
   git add .
   git commit -m "Description of the change"
   git push origin main
On render dashboard click manual deploy
Test the route
   
   


 
     

         



