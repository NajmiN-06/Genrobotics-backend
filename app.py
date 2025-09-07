#IMPORTS
from flask import Flask, request, jsonify, render_template 
from flask_sqlalchemy import SQLAlchemy
import os
import sqlite3
import json


#APP SETUP
app = Flask(__name__)
app.config['DEBUG'] = True

#CONFIGURE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///submissions.db'
db = SQLAlchemy(app)

VALID_PAGES = [
    "Bandicoot", "Bandicoot-Mobility", "G-Mammoth", "Wilboar",
        "G-Crow", "Sanitation-Infrastructure", "Confined-space-saftey", "Solution-for-unique-challenges"
]


#DATAMODEL
class ContactSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page_name = db.Column(db.String(100), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    organization = db.Column(db.String(150), nullable=False)
    message = db.Column(db.Text, nullable=False)    
with app.app_context():
    db.create_all()
print("The tables are created successfully")

#ROUTES
@app.route('/')
def home():
    return "Welcome to the backend of Genrobotics !"
@app.route('/submit/<page_name>', methods=['POST'])
def submit_form(page_name):
    try:
        if request.form:
            data = request.form
        else:
            data = request.json

        new_submission = ContactSubmission(
            page_name=page_name,
            full_name=data['full_name'],
            email=data['email'],
            organization=data['organization'],
            message=data['message']
        )

        db.session.add(new_submission)
        db.session.commit()

        result = {
            "page": page_name,
            "status": "success",
            "submitted_data": {
                "full_name": data['full_name'],
                "email": data['email'],
                "organization": data['organization'],
                "message": data['message']
            }
        }

        # Convert dict to formatted JSON string
        result_json = json.dumps(result, indent=4)

        return render_template("submission_result.html", result_json=result_json)

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500
#dynamic route 
@app.route('/<page_name>', methods=['GET'])
def service_page(page_name):
    if page_name not in VALID_PAGES:
        return render_template('404.html'), 404

    return render_template('form_template.html', page_name=page_name)



@app.route('/current-openings', methods=['GET'])
def current_openings():
    try:
        print("Connecting to database...")
        conn = sqlite3.connect('instance/submissions.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT Job_Title, Posting_Date, Job_Type, Job_Des, Location, Status
            FROM Current_Openings
        """)
        rows = cursor.fetchall()
        conn.close()
        print("Fetched rows:", rows)

        openings = [
            {
                "Job_Title": row[0],
                "Posting_Date": row[1],
                "Job_Type": row[2],
                "Job_Des": row[3],
                "Location": row[4],
                "Status": row[5]
            }
            for row in rows
        ]

        print("Formatted openings:", openings)
        return jsonify(openings), 200

    except Exception as e:
        print("Error occurred:", str(e))
        return jsonify({"error": str(e)}), 500


#RUNTHEAPP
 # Deployment fix: bind to 0.0.0.0 and dynamic port
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)












