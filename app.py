#IMPORTS
from flask import Flask, request, jsonify, render_template 
from flask_sqlalchemy import SQLAlchemy
import os


#APP SETUP
app = Flask(__name__)

#CONFIGURE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///submissions.db'
db = SQLAlchemy(app)

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
    return "Welcome to the backend of your company website!"
@app.route('/submit/<page_name>', methods=['POST'])
def submit_form(page_name):
    try:
        # Accept both JSON and form data
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

        return jsonify({"status": "success", "page": page_name})

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

#dynamic route 
@app.route('/<page_name>')
def render_form_page(page_name):
    valid_pages = [
        'Bandicoot', 'Bandicoot-Mobility', 'G-Mammoth', 'Wilboar',
        'G-Crow', 'Sanitation-Infrastructure', 'Confined-space-saftey', 'Solution-for-unique-challenges'
    ]
    if page_name not in valid_pages:
        return "Page not found", 404
    return render_template('form_template.html', page_name=page_name)


#RUNTHEAPP
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)








